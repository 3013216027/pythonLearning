# -*- coding:utf-8 -*-
# Author: zhengdongjian@tju.edu.cn
# Create Time: 2015年11月24日 12:32:06

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = open('gui-config.json', 'w')

import urllib
import urllib2
import string
import re
import json

url = 'http://www.ishadowsocks.com'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

try:
    req = urllib2.Request(url, headers = headers)
    res = urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        sys.stderr.write(e.code)
    if hasattr(e, 'reason'):
        sys.stderr.write(e.reason)
    exit()
if res is None:
    sys.stderr.write('Connection error!\n')
    exit()

content = res.read().decode('utf-8')
left = unicode.find(content, '"free"')
right = unicode.find(content, 'section', left)
content = content[left:right]

# print content
# 构造服务器配置表
# 每项为一个dic
configs = []
# ss, se
ss = 0
se = 0
keys = ['server', 'server_port', 'password', 'method', 'remarks']
while True:
    ss = unicode.find(content, 'col-lg-4', se)
    if (ss == -1):
        break
    else:
        se = unicode.find(content, 'div', ss)
    cfg = {}
    kvs = re.findall('<h4>.*?:(.*)</h4>', content[ss:se])
    idx = 0
    while idx < 4:
        if idx == 1:
            cfg[keys[idx]] = int(kvs[idx])
        else:
            cfg[keys[idx]] = str(kvs[idx])
        idx = idx + 1
    cfg[keys[idx]] = 'Server ' + str(len(configs) + 1)
    configs.append(cfg)
# print configs

# 构造配置文件
# configs: list L
# strategy: null
# index: 0,
# global: false
# enabled: true
# shareOverLan: true
# isDefault: false
# localPort: 6964
# pacUrl: null
# useOnlinePac: false
# availabilityStatistics: false
my = {}
my['configs'] = configs
my['strategy'] = None
my['index'] = 1
my['global'] = False
my['enabled'] = True
my['shareOverLan'] = True
my['isDefault'] = False
my['localPort'] = 6964
my['pacUrl'] = None
my['useOnlinePac'] = False
my['availabilityStatistics'] = False

json.dumps(my, indent = 1)
print json.dumps(my, indent = 1)
exit()

# print my
idx = 11
print '{'
for item in my:
    idx = idx - 1
    if idx == 0:
        print '"' + item + '": ' + str(my[item])
    else:
        print '"' + item + '": ' + str(my[item]) + ','
print '}'
