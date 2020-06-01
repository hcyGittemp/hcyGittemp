# -*- coding:utf-8 -*-
import unittest
#参数化-读取元组的值
import paramunittest
#读取配置信息
import readConfig as readConfig
#调用公共方法
from common import common
#调用-获取请求的封装方法
from common import configHttp
#日志打印
from common.Log import Logg

#实例化化调用
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
studentLogin_xls = common.get_xls("userCase.xlsx", "studentLogin")
log=Logg();
@paramunittest.parametrized(*studentLogin_xls)
class StudentLogin(unittest.TestCase):
    global log, logger, resultPath
    def setParameters(self, case_name, method, url, parameter, resultType, errno, error):
        #获取excel值
        self.case_name = str(case_name)
        self.method = str(method)
        self.url = str(url)
        self.parameter = str(parameter)
        self.resultType = str(resultType)
        self.errno = str(errno)
        self.error = str(error)

    #具体实现CASE
    def test_login(self):

        '''登录'''
        #self.url=/backend/app/unauth/login
        localConfigHttp.set_url(self.url)
        #/backend/student/unauth/login
        header = {"Content-Type": 'application/json'}
        localConfigHttp.set_headers(header)
        localConfigHttp.set_data(self.parameter)
        # 请求对应封装接口-json格式
        self.respon = localConfigHttp.postWithJson()
        # 调用checkResult验证方法
        print(self.respon.json())
        cc=self.respon.json()
        print(cc['error'])
        #self.checkResult();

    # # 较验json格式返回值
    # def checkResult(self):
    #     # 获取json格式值
    #     self.info = self.respon.json()
    #     #获取json值展示到报告中
    #     common.show_return_msg(self.respon)
    #     # 判断状态是否是200
    #     if self.resultType == '0' and self.respon.status_code == 200:
    #         self.assertEqual(self.info['errno'], int(self.errno))
    #         self.assertEqual(self.info['error'], "操作成功");
    #     if self.resultType == '1' and self.respon.status_code == 200:
    #         self.assertEqual(self.info['errno'], int(self.errno))
    #         self.assertEqual(self.info['error'], self.error);

if __name__ == '__main__':
    unittest.main()
