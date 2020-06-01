import unittest
import requests
import json
class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = {
            "phone": "14000000000",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "messageCode": "",
            "loginType": "1",
            "timestamp": ""
        }
        header = {"Content-Type": "application/json"}
        r = requests.post("http://api-shuangshi.tengyue360.com/backend/student/unauth/login", headers=header, json=data)
        msg=r.text
        dd=r.json()
        f=dd['errno']
        print(f)
        #想输出真正的中文需要指定ensure_ascii=False
        #indent=4 换行显示
        #sort_keys：将数据根据keys的值进行排序
        print(json.dumps(json.loads(msg)))
        print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    unittest.main()
