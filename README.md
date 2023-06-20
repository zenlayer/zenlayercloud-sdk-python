Quick Start[(中文)](./README-CN.md)

--- 

# Introduction

Welcome to Zenlayer Cloud API Software Developer Kit (SDK). SDK is a supporting tool for Zenlayer Cloud API. It currently supports Bare
Metal Instance, Elastic IP, DDoS Protected IP and other products. More cloud services will be supported for SDK.

# Requirements

1. The python environment is installed. version 3.6 or later is used.
2. A Zenlayer Cloud account is created and an Access Key ID and an Access Key Password are created.
   See [Generate an API Access Key](https://docs.console.zenlayer.com/welcome/platform/team-management/generate-an-api-access-key) for more
   details.

# Installation

## Installation with Pip (Recommended)

You can install the ZenlayerCloud API Python SDK into your project using the pip installation method. If your project environment does not have pip installed, please refer to the [pip](https://pip.pypa.io/en/stable/installation/) official website for detailed installation instructions.

To install or upgrade using pip, execute the following command in the command line:

```bash
pip install --upgrade zenlayercloud-sdk-python
```

Please note that if you have both Python 2 and Python 3 environments, the Python 3 environment should use the `pip3` command for installation.

## Installation from source

Go to the [Github repository](https://github.com/zenlayer/zenlayercloud-sdk-python) to download the latest code.

    $ cd zenlayercloud-sdk-python
    $ python setup.py install

```

# Examples

Take CreateInstances as an example.

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

# More Configuration

Before creating a client, you can configure the values of fields in the Config if needed.
```python
from zenlayercloud.common.config import Config

conf = Config()
```

The specific configuration options are explained below:

## Timeout
The SDK has a default timeout of 60 seconds. If needed, please refer to the code to get the latest default value. Unit: seconds
```python
from zenlayercloud.common.config import Config

conf = Config(debug=True)
conf.request_timeout = 120
```

## Debugging
You can enable debug mode, which will print more detailed logs (including request and response data). This can be useful for detailed error troubleshooting. Debug mode is disabled by default.

Default: False
```python
from zenlayercloud.common.config import Config

conf = Config(debug=True)
```

## Proxy

If you are in an environment with a proxy, you can set the proxy using the following method.
```python
from zenlayercloud.common.config import Config

conf = Config(proxy="http://host:port")
```
## Certificate Issue

When installing Python 3.6 or above on the Mac operating system, you may encounter a certificate error: `Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)`. This is because on Mac OS, Python no longer uses the system's default certificates and does not provide its own certificates. When making HTTPS requests, it requires the use of certificates provided by the `certifi` library. However, the SDK does not support specifying certificates, so the only solution is to install the certificates by running the command `sudo "/Applications/Python 3.6/Install Certificates.command"`.

The Python SDK uses the certificates provided by the `certifi` library by default. If you need to specify a certificate, you can do so with the following settings. If you want to skip certificate verification, pass `False` as the value.

```python
# Specify the certificate
conf = Config(certification="/path/to/certification")

# Skip certificate verification
conf = Config(certification=False)
```

---
Quick Start[(Chinese)](./README-CN.md)
