import datetime
import re
import requests
import urllib3
import argparse

urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument('-user', type=str, help="用户登录名/邮箱", dest="Username", default="")
parser.add_argument('-pass', type=str, help="用户登录密码", dest="Password", default="")
parser.add_argument('-q', type=str, help="查询语句", dest="Query", default="")
parser.add_argument('-p', type=int, help="查询数据页数(每页20条),初始值为1,最大值为20", dest="Page", default=1)
args = parser.parse_args()

access_token = ""
Total = ""
username = args.Username
password = args.Password
query = args.Query
page = args.Page

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'
}


def get_token():
    global access_token
    print("[+] 正在获取用户Token")
    data = '{"username":"%s","password": "%s"}' % (username, password)
    login_url = "https://api.zoomeye.org/user/login"
    try:
        res = requests.post(url=login_url, data=data, headers=header, verify=False)
        if "access_token" in res.json() and res.json()['access_token'] != "":
            access_token = res.json()['access_token']
            print("\033[32m[*] 用户Token获取成功\033[0m")
        else:
            print("\033[31m[-] 好像出了点问题，请检查一下账号和密码吧\033[0m")
            exit()
    except Exception as e:
        print("\033[31m[-] 好像出了点问题，请检查一下网络吧\033[0m")


def check_internet():
    print("[+] 正在检查您的网络")
    url = "https://2021.ip138.com/"
    try:
        res = requests.get(url=url, headers=header, verify=False, timeout=5)
        ip = re.findall("<title>(.*)</title>", res.text, re.IGNORECASE)[0].strip()
        add = re.findall("来自：(.*)", res.text, re.IGNORECASE)[0].strip()
        print("\033[32m[*] " + ip + " 来自：" + add + "\033[0m")
    except Exception as e:
        print("\033[31m[-] 似乎出了一点问题，请检查一下网络吧\033[0m")


def check_params():
    global page, username, password
    if isinstance(page, int):
        if page > 20:
            print("\033[31m[-] 开发太菜了，page最大等于20\033[0m")
            page = 20
        if query != "":
            if username != "" and password != "":
                check_internet()
                get_token()
                if access_token != "":
                    return True
                else:
                    print("\033[31m[-] 请先获取Token吧\033[0m")
                    exit()
            else:
                print("\033[31m[-] 好像出了点问题，请检查一下账号和密码吧\033[0m")
                exit()
        else:
            print("\033[31m[-] 缺少查询的语句\033[0m")
            exit()
    else:
        print("\033[31m[-] page应该是一个整数哦\033[0m")
        exit()


def get_urls():
    global page, Total
    header_token = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61',
        'Authorization': 'JWT ' + access_token
    }
    filename = result_filename()
    with open(filename, "w", encoding="utf-8") as f:
        get_url = "https://api.zoomeye.org/host/search?query=" + query
        page = page + 1
        for p_num in range(1, page):
            try:
                res = requests.get(url=get_url, headers=header_token, params={'page': p_num}, verify=False, timeout=20)
                if Total == "" and "flag" not in Total:
                    Total = str(res.json()['total'])
                    print("\033[32m[*] " + query + "搜索结果共有数据" + Total + "条\033[0m")
                    if Total == "0":
                        exit()
                    Total += "flag"
                print("\033[32m[*] [-----------> 正在获取第" + str(p_num) + "页内容 <-----------]\033[0m")
                for i in range(len(res.json()['matches'])):
                    ip = res.json()['matches'][i]['ip']
                    port = res.json()['matches'][i]['portinfo']['port']
                    service = res.json()['matches'][i]['portinfo']['service']
                    if "-proxy" in str(service):
                        service = str(service).replace("-proxy", "")
                    web_server = str(res.json()['matches'][i]['portinfo']['app']).replace("null", "无Webserver")
                    if len(web_server) > 15:
                        web_server = web_server[:15]
                    title = str(res.json()['matches'][i]['portinfo']['title']).replace("null", "无标题")
                    if len(title) > 50:
                        title = title[:51]
                    url = str(service) + "://" + str(ip) + ":" + str(port) + "/"
                    f.write(url + "\n")
                    print("%-32s%-15s%-50s" % (url, web_server, title))
            except Exception as e:
                print("\033[31m[-] 第" + str(p_num) + "页获取失败，正在获取" + str(p_num + 1) + "页\033[0m")
                continue
        print("\033[32m[+] 结果已保存至" + filename + "\033[0m")


def result_filename():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    filename = str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + "-" + str(minute) + ".txt"
    return filename


def menu():
    print("\033[32m********************************************************************\033[0m")
    print("\033[32m    * * * *  * * * *  * * * *  *     *  * * * *  *     *  * * * *   \033[0m")
    print("\033[32m        *    *     *  *     *  **   **  *         *   *   *         \033[0m")
    print("\033[32m      *      *     *  *     *  * * * *  * * * *     *     * * * *   \033[0m")
    print("\033[32m    *        *     *  *     *  *  *  *  *           *     *         \033[0m")
    print("\033[32m    * * * *  * * * *  * * * *  *     *  * * * *     *     * * * *   \033[0m")
    print("\033[32m      --Coded by adminsec5247        https://github.com/adminsec5247\033[0m")
    print("\033[32m********************************************************************\033[0m")


def start():
    menu()
    if check_params():
        get_urls()


if __name__ == '__main__':
    start()
