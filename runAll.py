import os
import unittest
#导入log模块
from common.Log import Logg
#读取配置信息
import readConfig as readConfig
#生成excel报告
from common import HTMLTestRunner
#实例化调用读取配置信息
localReadConfig = readConfig.ReadConfig()
#调用LOG方法
cc=Logg();
class AllTest:
    #初始化值,获取各个路径,设置全局变量
    def __init__(self):
        global logger, resultPath
        logger = cc.get_logger();
        #获取报告路径
        resultPath = cc.get_report_path()
        #C:\Users\Administrator\Desktop\interfaceTest\result\report.html
        #得到文件的路径/caselist.txt
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        #self.caseListFile=C:\Users\Administrator\Desktop\interfaceTest\caselist.txt
        #获取文件的名字路径
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        #self.caseFile=C:\Users\Administrator\Desktop\interfaceTest\testCase
        #定义了空列表
        self.caseList = []
        #user/testStudentLogin user/testqueryStudentById
    #设置执行的case
    def set_case_list(self):
        #获取caselist文件打开它
        fb = open(self.caseListFile)
         #循环读取caselist.txt文件的名字
         #例如：user/testStudentLogin
        for value in fb.readlines():
            #获取data值 user/testStudentLogin
            data = str(value)
            #startswit 排除开始是#的内容  endswith 排除开始是xx内容
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    #设置测试套件
    def set_case_suite(self):
        self.set_case_list()
        #创建一个测试套件
        test_suite = unittest.TestSuite()
        #定义了个空列表
        suite_module = []
        #self.caseList = ['user/testStudentLogin', 'user/testqueryStudentById']
        for case in self.caseList:
            #截取后缀user/的testStudentLogin
            case_name = case.split("/")[-1]
            ##定义测试目录为当前目录备注： https://www.cnblogs.com/klb561/p/9315127.html
            #top_level_dir = None ：测试模块的顶层目录，如果没有顶层目录，默认为None
            #discover方法会自动根据测试目录test_dir匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中

            #self.caseFile=要测试的模块名或测试用例目录
            #pattern=表示用例文件名的匹配原则
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                test_suite.addTest(suite)
        else:
            return None
        return test_suite

    #报告执行
    def run(self):
        try:
            #执行测试套件
            suit = self.set_case_suite()
            #打印日志信息
            if suit is not None:
                logger.info("********TEST START********")
                #定义测试报告
                fp = open(resultPath,'wb')
                #执行测试报告
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"XIAOR接口测试报告", description=u"用例执行情况")
                #运行测试用例
                runner.run(suit);
            else:
                logger.info("没有测试案例")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("测试结束")
            fp.close()
if __name__ == '__main__':
    obj = AllTest();
    obj.run();
