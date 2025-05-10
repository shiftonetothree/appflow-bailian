# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_bailian20231229.client import Client as bailian20231229Client
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bailian20231229 import models as bailian_20231229_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_credentials.models import Config

workspace_id = os.getenv("BAILIAN_WORKSPACE_ID")

class Bailian:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> bailian20231229Client:
        """
        使用凭据初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码建议使用更安全的无AK方式，凭据配置方式请参见：https://help.aliyun.com/document_detail/378659.html。
        credential = CredentialClient()
        config = open_api_models.Config(
            credential=credential
        )
        # Endpoint 请参考 https://api.aliyun.com/product/bailian
        config.endpoint = f'bailian.cn-beijing.aliyuncs.com'
        return bailian20231229Client(config)

    @staticmethod
    def create_memory_with_options(
        description
    ) -> None:
        client = Bailian.create_client()
        create_memory_request = bailian_20231229_models.CreateMemoryRequest()
        create_memory_request.description = description
        runtime = util_models.RuntimeOptions()
        headers = {}
        try:
            # 复制代码运行请自行打印 API 的返回值
            result = client.create_memory_with_options(workspace_id, create_memory_request, headers, runtime)
            memory = result.body
            return memory
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
    @staticmethod
    def list_memories_with_options(
        description
    ) -> None:
        client = Bailian.create_client()
        list_memories_request = bailian_20231229_models.ListMemoriesRequest()
        list_memories_request.max_results = 50
        runtime = util_models.RuntimeOptions()
        headers = {}
        try:
            # 复制代码运行请自行打印 API 的返回值
            memories = client.list_memories_with_options(workspace_id, list_memories_request, headers, runtime)
            print(memories)
            memories = memories.body.memories
            memory = None
            for item in memories:
                print(item)
                if item.description == description:
                    memory = item
            return memory
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)
