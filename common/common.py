import requests
#获取config里面的信息
#as别名
import readConfig as readConfig
import os
#读取excel
from xlrd import open_workbook
from common.Log import Logg
log=Logg()#调用初始化
import json
#导入方法读取baseurl
localReadConfig = readConfig.ReadConfig()
#localReadConfig.get_http("port")
#print(localReadConfig)
#获取文件的路径
proDir = readConfig.proDir

#获取登陆token 公共方法
def get_visitor_token():
    send_param = {
          "phone":"14000000000",
          "password":"e10adc3949ba59abbe56e057f20f883e",
          "messageCode":"",
          "source":"2",
          "loginType":1
        }

    #优化精简方式
    urllist = localReadConfig.get_http("BASEURL")
    headers = {"Content-Type": 'application/json'}
    #字符串转换为json格式-data=json.dumps(send_parm)
    #res=requests.post("https://api-shuangshi.tengyue360.com/backend/app/unauth/login")
    res = requests.post("https://"+urllist + "/backend/app/unauth/login",json=send_param, headers=headers)
    #输出json值
    info = res.json()
    #header中获取token
    token=res.headers['Authorization']
    return token

#每个接口报告返回的信息值
def show_return_msg(response):
    # 返回response返回信息
    url = response.url
    # 返回json返回值
    msg = response.text
    print("\n请求地址：" + url)
    # 可以显示中文输出真正的中文需要指定ensure_ascii=False sort_keys=Tru将数据根据keys的值进行排序
    #indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json
    print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))

# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # 获取xls文件的路径
    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
    #D:\interfaceTest\testFile\case\userCase.xlsx
    # 打开文件
    file = open_workbook(xlsPath)
    # 按照名称获取工作列表
    sheet = file.sheet_by_name(sheet_name)
    # 获取页的一行
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

if __name__ == "__main__":
    get_visitor_token();
