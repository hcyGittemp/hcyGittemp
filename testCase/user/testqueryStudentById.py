# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import unittest
import paramunittest
import readConfig as readConfig
from common import common
from common import configHttp
from common.Log import Logg
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
queryStudentById_xls = common.get_xls("userCase.xlsx", "queryStudentById")
log=Logg()
@paramunittest.parametrized(*queryStudentById_xls)
# 根据学员ID查询学员  http://api-shuangshi.tengyue360.com/backend/student/student/queryStudentById
class QueryStudentById(unittest.TestCase):
    #初始化赋值
    def setParameters(self, case_name, method, url, parameter, resultType, status, error, message):
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.parameter = str(parameter)
        self.resultType = str(resultType)
        self.status= status
        self.error = str(error)
        self.message = str(message)

    #具体实现用例
    def test_QueryStudentById(self):
        '''查询学员信息接口'''
        localConfigHttp.set_url(self.url)
        # 获取commontoken信息
        token_v = common.get_visitor_token()
        header = {"Content-Type": 'application/json', "authorization": token_v}
        localConfigHttp.set_headers(header)
        # set param
        localConfigHttp.set_data(self.parameter)
        # 请求对应封装接口
        self.respon = localConfigHttp.postWithJson()
        # 调用checkResult方法
        self.checkResult()

    # 较验json格式返回值
    def checkResult(self):
        # 获取json格式值
        self.info = self.respon.json()
        common.show_return_msg(self.respon)
        # 判断状态是否是200
        # 断言返回值errno, cityname,error是否成功
        self.assertEqual(self.info['status'], 404)
        self.assertEqual(self.info['error'], self.error)
        self.assertEqual(self.info['message'], "No message available")
