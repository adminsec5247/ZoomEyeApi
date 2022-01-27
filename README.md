# 一、ZoomEyeApi介绍
Zoom Eye API是一款钟馗之眼(ZoomEye)接口工具，只需要简单的命令或配置，即可快速获取资产。
# 二、使用需求
Python 3并且需要安装以下module

`pip3 install requests,argparse,re`
# 三、使用方法
切换到工具所在目录，命令行执行以下命令即可

`python3 ZoomEyeApi.py -user [username] -pass [password] -q [query] -p [page]`

查看帮助
“python3 ZoomEyeApi.py -h”

options:

  -h, --help      		show this help message and exit
  
  -user [USERNAME]  	用户登录名/邮箱
  
  -pass [PASSWORD]  	用户登录密码
  
  -q [QUERY]        	查询语句
  
  -p [PAGE]         	查询数据页数(每页20条),初始值为1,最大值为20
  # 四、工具演示
  工具自动补全URL，并且展示一些常规信息，方便筛选目标
  
  ![演示图片1](https://github.com/adminsec5247/ZoomEyeApi/blob/main/image/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%871.png "演示")
  
  结果以单纯的URL格式保存，方便后续批量操作
  
  ![演示图片2](https://github.com/adminsec5247/ZoomEyeApi/blob/main/image/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%872.png "演示")
  # 五、备注与注意
  工具可以在代码中保存用户的账号和密码，省去每次运行都输入账号密码的繁琐。在代码default中添加对应的账号密码即可。同样的其他参数也可以添加初始值，看个人喜好。
  
  ![演示图片3](https://github.com/adminsec5247/ZoomEyeApi/blob/main/image/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%873.png "演示")
  
  工具在Linux操作系统稳定运行，在Windows操作系统上可能会出现乱码，这里提供两种解决方案。一是删除颜色输出的代码“\033[31m”与“\033[0m”以及“\033[32m”；二是参考文章
  [cmd /033转义字符对输出内容进行颜色变化出现乱码的解决办法](https://www.pythonheidong.com/blog/article/450666/ae3c61b58b57078dfdbe/)
  
  在[https://github.com/adoxa/ansicon/releases](https://github.com/adoxa/ansicon/releases)下载工具
  ![备注图片1](https://github.com/adminsec5247/ZoomEyeApi/blob/main/image/%E5%A4%87%E6%B3%A8%E5%9B%BE%E7%89%871.png "备注")
  
  下载后解压，选择合适的版本，然后在CMD运行下面的两条命令即可
  
  `ansicon.exe -i`
  
  `ansicon.exe -l`
