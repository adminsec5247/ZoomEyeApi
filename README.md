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
  # 工具演示
  工具自动补全URL，并且展示一些常规信息，方便筛选目标
  
  
