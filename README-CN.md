快速使用[(English)](./README.md)

--- 

# 简介

欢迎使用Zenlayer Cloud 开发者工具SDK，SDK是云 Zenlayer API
平台v2版本的配套工具。目前已经支持bmc、vm等产品，后续所有的云服务产品都会接入进来。
为方便 Python 开发者调试和接入 Zenlayer Cloud 产品 API，提供了一些使用SDK的简单示例。让您快速上手调试 Python SDK。

# 依赖环境

1. 依赖环境：Python 3.6+ 版本。
2. 要使用 Zenlayer Cloud Python, 您需要在云平台拥有一个云账号，并在 Zenlayer 云平台控制台中的创建和查看您的 Access Key ID 和 Access Key
   Password。如何获取详见 [帮助文档](https://docs.console.zenlayer.com/welcome/platform/team-management/generate-an-api-access-key)

# 获取安装

## 通过 Pip 安装(推荐)

您可以通过 pip 安装方式将ZenlayerCloud API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip](https://pip.pypa.io/en/stable/installation/)官网 安装。

通过pip方式安装或更新请在命令行中执行以下命令:

```bash
pip install --upgrade zenlayercloud-sdk-python
```

请注意，如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

## 通过源码包安装

前往 [Github 仓库](https://github.com/zenlayer/zenlayercloud-sdk-python) 下载最新代码

    $ cd zenlayercloud-sdk-python
    $ python setup.py install


# 快速使用

以BMC服务产品下创建实例接口CreateInstances为例：

```python
from zenlayercloud.bmc.v20221120 import bmc_client, models
from zenlayercloud.bmc.v20221120.models import InstanceChargePrepaid
from zenlayercloud.common.config import Config
from zenlayercloud.common.credential import Credential
from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException

if __name__ == '__main__':
   logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s', level=logging.DEBUG)
   
   try:
     credential = Credential("< Your AccessKeyId >", "< Your AccessKeyPassword >")
     config = Config(debug=True)
   
     client = bmc_client.BmcClient(credential=credential, config=config)
   
     print(InstanceChargePrepaid({"period": 1}).serialize())
     request = models.CreateInstancesRequest()
     request.zoneId = "SEL-A"
     request.instanceChargeType = "PREPAID"
     request.instanceTypeId = "S8A"
     request.internetChargeType = "ByBandwidth"
     request.instanceChargePrepaid = InstanceChargePrepaid({"period": 1})
   
     response = client.CreateInstances(request)
     print(response)
   except ZenlayerCloudSdkException as err:
     print(err)
```

# 相关配置
在创建客户端前，如有需要，Config 中字段的值进行一些配置。
```python
from zenlayercloud.common.config import Config

conf = Config()
```
具体的配置项说明如下：

## 超时时间
SDK有默认的超时时间,默认为60秒。 如有需要请在代码中查阅以获取最新的默认值。 单位：秒
```python
conf.request_timeout = 120
```

## 调试
你可以设置开启调试模式，调试模式会打印更详细的日志(包括请求和响应数据），当您需要进行详细的排查错误时可以开启。默认调试模式为关闭。

默认为 False
```python
from zenlayercloud.common.config import Config

conf = Config(debug=True)
```

## 代理

如果是有代理的环境下，可通过以下方式设置代理

```python
from zenlayercloud.common.config import Config

conf = Config(proxy="http://host:port")
```

## 证书问题

在 Mac 操作系统安装 Python 3.6 或以上版本时，可能会遇到证书错误：`Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).`。这是因为在 Mac 操作系统下，Python 不再使用系统默认的证书，且本身也不提供证书。在进行 HTTPS 请求时，需要使用 `certifi` 库提供的证书，但 SDK 不支持指定，所以只能使用 `sudo "/Applications/Python 3.6/Install Certificates.command"` 命令安装证书才能解决此问题。

python sdk默认使用 certifi 库提供的证书，如需要指定证书可以进行如下设置，若想跳过证书则传入 False
```python
# 指定证书
conf = Config(certification="/path/to/certification")

# 跳过证书校验
conf = Config(certification=False)
```

---
快速使用[(English)](./README.md)
