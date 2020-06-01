import requests
import readConfig as readConfig

#实例化调用
localReadConfig = readConfig.ReadConfig()

#初始化配置信息，以及请求URL公共方法的一些封装
class ConfigHttp:
    #获取url配置相关信息/相关json/get/post方法定义
    def __init__(self):
        #全局变量
        global scheme, urlhost, port, timeout
        scheme = localReadConfig.get_http("scheme")
        urlhost = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")

        #定义字典
        self.url={}
        self.headers = {}
        self.params = {}
        self.data = {}
        self.files = {}


    #写入值
    def set_url(self, url):
        self.url = scheme+'://'+urlhost+url
        #self.url="http://api-shuangshi.tengyue360.com/backend/student/unauth/login"

    def set_headers(self, header):
        self.headers = header
       #self.headers="Content-Type": 'application/json'

    def set_params(self, param):
        self.params = param
    #   #  send_param = {"phone": self.phone, "password": self.password, "messageCode": self.messageCode,"loginType": self.loginType, "timestamp": self.timestamp}

    def set_data(self, data):
        self.data = data

    # get公共方法封装
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, timeout=float(timeout))
            return response
        except TimeoutError:
            #none没有值
            return None

    #定义post方法
    def post(self):
        try:
            response = requests.post(self.url, data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            return None

    #定义post上传方法
    def postWithFile(self):
        try:
            response = requests.post(self.url, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            return None

    #定义请求post json格式方法
    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers,data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            return None

if __name__ == "__main__":
    print("ConfigHTTP")
