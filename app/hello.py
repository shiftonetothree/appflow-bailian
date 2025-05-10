import os
from flask import Flask
from flask import request
from http import HTTPStatus
from dashscope import Application
from . import bailian

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello_world():
    # return 'ok';
    prompt = request.args['prompt']
    userId = request.args['userId']
    memory = bailian.Bailian.list_memories_with_options(userId)
    if memory is None:
        memory = bailian.Bailian.create_memory_with_options(userId) 
    print(memory)
    return call_with_session(prompt,memory.memory_id)
    # return 'ok'
    

app_id = os.getenv("BAILIAN_APP_ID")

def call_with_session(prompt,memory_id):
    response = Application.call(
        # 若没有配置环境变量，可用百炼API Key将下行替换为：api_key="sk-xxx"。但不建议在生产环境中直接将API Key硬编码到代码中，以减少API Key泄露风险。
        # api_key=api_key,
        app_id=app_id,  # 替换为实际的应用 ID
        prompt=prompt,
        memory_id=memory_id,)

    if response.status_code != HTTPStatus.OK:
        print(f'request_id={response.request_id}')
        print(f'code={response.status_code}')
        print(f'message={response.message}')
        print(f'请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code')
    return response.output