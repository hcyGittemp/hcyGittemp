接口自动化1.0版本
 
目录 结构：
common：存放一些公共通用的方法
    common
    1.登录接口获取TOKEN-公共方法
    2.报告中中用例的返回值以及url-公共方法
    3.获取excel用例值放入一个列表中-公共方法
     
	confighttp 
	 第一个获取相关config.ini 配置信息
	 封装get post方法
	log模块：
	第一：创建报告文件夹到指定路径
	第二：封装log模块
	
result：执行过程中生成的文件夹，里面存放每次测试的结果
testCase：用于存放具体的测试case
testFile：存放测试过程中用到的文件，包括上传的文件，测试用例
caselist：txt文件，配置每次执行的case名称
config：配置一些常量，例如数据库的相关信息，接口的相关信息参数等
readConfig： 用于读取config配置文件中的内容
runAll：用于执行case


 接口自动测试流程->抓包/postman使用->requests->logging->配置文件读取->excel等等-》到搭建-〉项目持续集成妥妥的

 ###############################################################