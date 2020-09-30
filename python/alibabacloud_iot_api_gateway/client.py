# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.request import TeaRequest
from Tea.exceptions import TeaException, UnretryableException
from Tea.core import TeaCore

from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_apigateway_util.client import Client as APIGatewayUtilClient


class Client(object):
    """
    test
    """
    def __init__(self, config, _app_key=None, _app_secret=None, _protocol=None, _user_agent=None, _read_timeout=None,
                 _connect_timeout=None, _http_proxy=None, _https_proxy=None, _no_proxy=None, _max_idle_conns=None, _domain=None):
        self._app_key = _app_key        # type: str
        self._app_secret = _app_secret  # type: str
        self._protocol = _protocol      # type: str
        self._user_agent = _user_agent  # type: str
        self._read_timeout = _read_timeout  # type: int
        self._connect_timeout = _connect_timeout  # type: int
        self._http_proxy = _http_proxy  # type: str
        self._https_proxy = _https_proxy  # type: str
        self._no_proxy = _no_proxy      # type: str
        self._max_idle_conns = _max_idle_conns  # type: int
        self._domain = _domain          # type: str
        self._domain = config.domain
        self._app_key = config.app_key
        self._app_secret = config.app_secret
        self._protocol = config.protocol
        self._read_timeout = config.read_timeout
        self._connect_timeout = config.connect_timeout
        self._http_proxy = config.http_proxy
        self._https_proxy = config.https_proxy
        self._no_proxy = config.no_proxy
        self._max_idle_conns = config.max_idle_conns

    def do_request(self, pathname, protocol, method, header, body, runtime):
        """
        Send request

        @type pathname: str
        @param pathname: the url path

        @type protocol: str
        @param protocol: http or https

        @type method: str
        @param method: example GET

        @type header: dict
        @param header: request header

        @param body: the object of IoTApiRequest

        @param runtime: which controls some details of call api, such as retry times

        @return: the response
        """
        body.validate()
        runtime.validate()
        _runtime = {
            "timeouted": "retry",
            "readTimeout": UtilClient.default_number(runtime.read_timeout, self._read_timeout),
            "connectTimeout": UtilClient.default_number(runtime.connect_timeout, self._connect_timeout),
            "httpProxy": UtilClient.default_string(runtime.http_proxy, self._http_proxy),
            "httpsProxy": UtilClient.default_string(runtime.https_proxy, self._https_proxy),
            "noProxy": UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            "maxIdleConns": UtilClient.default_number(runtime.max_idle_conns, self._max_idle_conns),
            "retry": {
                "retryable": runtime.autoretry,
                "maxAttempts": UtilClient.default_number(runtime.max_attempts, 3)
            },
            "backoff": {
                "policy": UtilClient.default_string(runtime.backoff_policy, "no"),
                "period": UtilClient.default_number(runtime.backoff_period, 1)
            },
            "ignoreSSL": runtime.ignore_ssl
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, protocol)
                _request.method = UtilClient.default_string(method, "POST")
                _request.pathname = pathname
                _request.headers = TeaCore.merge({
                    "host": self._domain,
                    "date": UtilClient.get_date_utcstring(),
                    "x-ca-nonce": UtilClient.get_nonce(),
                    "x-ca-key": self._app_key,
                    "x-ca-signaturemethod": "HmacSHA256",
                    "accept": "application/json",
                    "user-agent": self.get_user_agent()
                }, header)
                if UtilClient.empty(body.id):
                    body.id = UtilClient.get_nonce()
                if not UtilClient.is_unset(body):
                    _request.headers["content-type"] = "application/octet-stream"
                    _request.headers["content-md5"] = APIGatewayUtilClient.get_content_md5(UtilClient.to_jsonstring(body.to_map()))
                    _request.body = UtilClient.to_jsonstring(body.to_map())
                _request.headers["x-ca-signature"] = APIGatewayUtilClient.get_signature(_request, self._app_secret)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                return _response
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get_user_agent(self):
        """
        Get user agent

        @rtype: str
        @return: user agent
        """
        user_agent = UtilClient.get_user_agent(self._user_agent)
        return user_agent
