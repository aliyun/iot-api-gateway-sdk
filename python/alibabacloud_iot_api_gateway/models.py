# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, Any
except ImportError:
    pass


class Config(TeaModel):
    def __init__(self, domain=None, protocol=None, app_key=None, app_secret=None, token=None, region_id=None,
                 read_timeout=None, connect_timeout=None, local_addr=None, http_proxy=None, https_proxy=None, no_proxy=None,
                 max_idle_conns=None):
        self.domain = domain            # type: str
        self.protocol = protocol        # type: str
        self.app_key = app_key          # type: str
        self.app_secret = app_secret    # type: str
        self.token = token              # type: str
        self.region_id = region_id      # type: str
        self.read_timeout = read_timeout  # type: int
        self.connect_timeout = connect_timeout  # type: int
        self.local_addr = local_addr    # type: str
        self.http_proxy = http_proxy    # type: str
        self.https_proxy = https_proxy  # type: str
        self.no_proxy = no_proxy        # type: str
        self.max_idle_conns = max_idle_conns  # type: int

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.app_key, 'app_key')
        self.validate_required(self.app_secret, 'app_secret')

    def to_map(self):
        result = {}
        result['domain'] = self.domain
        result['protocol'] = self.protocol
        result['appKey'] = self.app_key
        result['appSecret'] = self.app_secret
        result['token'] = self.token
        result['regionId'] = self.region_id
        result['readTimeout'] = self.read_timeout
        result['connectTimeout'] = self.connect_timeout
        result['localAddr'] = self.local_addr
        result['httpProxy'] = self.http_proxy
        result['httpsProxy'] = self.https_proxy
        result['noProxy'] = self.no_proxy
        result['maxIdleConns'] = self.max_idle_conns
        return result

    def from_map(self, map={}):
        self.domain = map.get('domain')
        self.protocol = map.get('protocol')
        self.app_key = map.get('appKey')
        self.app_secret = map.get('appSecret')
        self.token = map.get('token')
        self.region_id = map.get('regionId')
        self.read_timeout = map.get('readTimeout')
        self.connect_timeout = map.get('connectTimeout')
        self.local_addr = map.get('localAddr')
        self.http_proxy = map.get('httpProxy')
        self.https_proxy = map.get('httpsProxy')
        self.no_proxy = map.get('noProxy')
        self.max_idle_conns = map.get('maxIdleConns')
        return self


class CommonParams(TeaModel):
    def __init__(self, api_ver=None, iot_token=None, cloud_token=None, language=None, locale=None):
        # API版本
        self.api_ver = api_ver          # type: str
        # 登录用户的token(客户端)
        self.iot_token = iot_token      # type: str
        # 云端资源token（云端)
        self.cloud_token = cloud_token  # type: str
        # 国际化扩展，语言
        self.language = language        # type: str
        # 国际化扩展，地理位置、ip
        self.locale = locale            # type: str

    def validate(self):
        self.validate_required(self.api_ver, 'api_ver')

    def to_map(self):
        result = {}
        result['apiVer'] = self.api_ver
        result['iotToken'] = self.iot_token
        result['cloudToken'] = self.cloud_token
        result['language'] = self.language
        result['locale'] = self.locale
        return result

    def from_map(self, map={}):
        self.api_ver = map.get('apiVer')
        self.iot_token = map.get('iotToken')
        self.cloud_token = map.get('cloudToken')
        self.language = map.get('language')
        self.locale = map.get('locale')
        return self


class IoTApiRequest(TeaModel):
    def __init__(self, id=None, version=None, params=None, request=None):
        # 一次请求的标示，用于请求跟踪问题排查
        self.id = id                    # type: str
        # 协议版本
        self.version = version          # type: str
        # JSON对象，访问指定api的业务参数
        self.params = params            # type: Dict[str, Any]
        # JSON对象，与业务无关的通用参数
        self.request = request          # type: CommonParams

    def validate(self):
        self.validate_required(self.request, 'request')
        if self.request:
            self.request.validate()

    def to_map(self):
        result = {}
        result['id'] = self.id
        result['version'] = self.version
        result['params'] = self.params
        if self.request is not None:
            result['request'] = self.request.to_map()
        else:
            result['request'] = None
        return result

    def from_map(self, map={}):
        self.id = map.get('id')
        self.version = map.get('version')
        self.params = map.get('params')
        if map.get('request') is not None:
            temp_model = CommonParams()
            self.request = temp_model.from_map(map['request'])
        else:
            self.request = None
        return self
