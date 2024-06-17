# 获取实例信息列表文档示例

该项目为调用ListInstances接口，获取实例信息列表。文档示例，该示例**无法在线调试**，如需调试可下载到本地后替换 [AK](https://usercenter.console.aliyun.com/#/manage/ak) 以及参数后进行调试。

## 运行条件

- 下载并解压需要语言的代码;


- 在阿里云帐户中获取您的 [凭证](https://usercenter.console.aliyun.com/#/manage/ak)并通过它替换下载后代码中的 ACCESS_KEY_ID 以及 ACCESS_KEY_SECRET;

- 执行对应语言的构建及运行语句

## 执行步骤

下载的代码包，在根据自己需要更改代码中的参数和 AK 以后，可以在**解压代码所在目录下**按如下的步骤执行

- Python
- *Python 版本要求 Python3*
```sh
python3 setup.py install && python ./alibabacloud_sample/sample.py
```
## 使用的 API

-  ListInstances 调用ListInstances接口，获取实例信息列表。文档示例，可以参考：[文档](https://next.api.aliyun.com/document/dms-enterprise/2018-11-01/ListInstances)

## 返回示例

*实际输出结构可能稍有不同，属于正常返回；下列输出值仅作为参考，以实际调用为准*


- JSON 格式 
```js
{
  "TotalCount": 7,
  "RequestId": "98D35416-2B92-4CE5-8FD2-B1E61E165536",
  "Success": true,
  "InstanceList": {
    "Instance": [
      
    ]
  }
}
```
- XML 格式 
```xml
<TotalCount>7</TotalCount>
<RequestId>98D35416-2B92-4CE5-8FD2-B1E61E165536</RequestId>
<Success>true</Success>
<InstanceList>
</InstanceList>
```

