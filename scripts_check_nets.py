# 作者仓库:https://github.com/spiritLHL/qinglong_auto_tools
# 觉得不错麻烦点个star谢谢


'''
cron: 1
new Env('二叉树查脚本网络链接');
'''



# 主青龙，需要查找网络链接的容器，事先需要在容器里创建应用，给所有权限，然后重启容器，应用设置才会生效，
cilent_id1 = ""
cilent_secret1 = ""
url1 = ""

expect_list = [url1, ""] # 不需要被查询的链接，比如你的网址


# 屏蔽词
keys = []

# 屏蔽词也可在fake_keys.txt中按一行一行填写
with open("fake_keys.txt", "r") as fp:
    t = fp.readlines()

for i in t:
    keys.append(i)

keys = list(set(keys))

import requests
import time
import json
import re

requests.packages.urllib3.disable_warnings()


def gettimestamp():
    return str(int(time.time() * 1500))


def gettoken(self, url_token):
    r = requests.get(url_token).text
    res = json.loads(r)["data"]["token"]
    self.headers.update({"Authorization": "Bearer " + res})


def login(self, baseurl, cilent_id_temp, cilent_secret_temp):
    url_token = baseurl + 'open/auth/token?client_id=' + cilent_id_temp + '&client_secret=' + cilent_secret_temp
    gettoken(self, url_token)


def getitem(self, baseurl, typ):
    url = baseurl + typ + "/scripts/files?t=%s" % gettimestamp()
    r = self.get(url)
    item = json.loads(r.text)["data"]
    return item


def getscript(self, baseurl, typ, filename):
    url = baseurl + typ + "/scripts/" + filename + "?t=%s" % gettimestamp()
    r = self.get(url)
    script = json.loads(r.text)["data"]
    return script


def pushscript(self, baseurl, typ, data):
    url = baseurl + typ + "/scripts?t=%s" % gettimestamp()
    self.headers.update({"Content-Type": "application/json;charset=UTF-8", 'Connection': 'close'})
    r = self.put(url, data=json.dumps(data))
    # response = json.loads(r.text)["data"]
    return r


def getcrons(self, baseurl, typ):
    url = baseurl + typ + "/crons?t=%s" % gettimestamp()
    r = self.get(url)
    item = json.loads(r.text)["data"]
    return item


def addcron(self, baseurl, typ, data):
    url = baseurl + typ + "/crons?t=%s" % gettimestamp()
    self.headers.update({"Content-Type": "application/json;charset=UTF-8", 'Connection': 'close'})
    r = self.post(url, data=json.dumps(data))
    if json.loads(r.text)["code"] == 200:
        return True
    else:
        return r.text


if __name__ == '__main__':
    # 主容器
    s = requests.session()
    login(s, url1, cilent_id1, cilent_secret1)

    # 获取主青龙任务
    print("=========== 主青龙 信息获取中 =============")
    print()

    # 获取主青龙的脚本名
    zscripts = getitem(s, url1, "open")
    zscripts_list = []
    for i in zscripts:
        zscripts_list.append(i["key"])
    try:
        zscripts.remove("fake_keys.txt")
    except:
        print("fake_keys.txt 不在脚本列表里\n")
    print("主青龙脚本文件数量：{}".format(len(zscripts_list)))
    print()
    print()

    print("获取脚本文件内容")

    data_script_list = []
    for i in zscripts_list:
        content = getscript(s, url1, "open", i)
        data_script_list.append(content)

    # 筛出网址

    print()
    print("查询脚本，筛选网址中")
    print()

    net_list = []
    for i in data_script_list:
        temp = re.findall(r"\"https://(.*?)\"", i)
        for j in temp:
            net_list.append(j)

    for i in data_script_list:
        temp = re.findall(r"\"http://(.*?)\"", i)
        for j in temp:
            net_list.append(j)

    for i in data_script_list:
        temp = re.findall(r"\'https://(.*?)\'", i)
        for j in temp:
            net_list.append(j)

    for i in data_script_list:
        temp = re.findall(r"\'http://(.*?)\'", i)
        for j in temp:
            net_list.append(j)

    net_l = list(set(net_list))
    nets = []
    for i in net_l:
        if ".jd.com" not in i and "." in i and i not in expect_list:
            nets.append(i)

    # 输出找到的链接
    net = list(set(nets))
    for k in net:
        print(k)

    print()
    print("查到链接个数： {}".format(len(net)))

    cct = 0
    for n in nets:
        for j in keys:
            if j in n:
                cct +=1

    print()
    print("包含屏蔽词链接个数： {}".format(cct))

    print()
    print("查询结束")














