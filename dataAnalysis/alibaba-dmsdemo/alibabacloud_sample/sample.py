# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_dms_enterprise20181101.client import Client as dms_enterprise20181101Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dms_enterprise20181101 import models as dms_enterprise_20181101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dms_enterprise20181101Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['LTAI5tKQh6CTWqAQtKM8k3RU'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['srCPRNjzi0cw5abarSKJweMCmHQWwm']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/dms-enterprise
        config.endpoint = f'dms-enterprise.cn-hangzhou.aliyuncs.com'
        return dms_enterprise20181101Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_instances_request = dms_enterprise_20181101_models.ListInstancesRequest()
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.list_instances_with_options(list_instances_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_instances_request = dms_enterprise_20181101_models.ListInstancesRequest()
        runtime = util_models.RuntimeOptions()
        try:
            resp = await client.list_instances_with_options_async(list_instances_request, runtime)
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
