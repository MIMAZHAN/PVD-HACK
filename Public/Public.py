# -*- coding: utf-8 -*-
import copy
import time

# 参数修改的逻辑：
def queryValue(query):
    dokey = []
    rearray = []
    for key, value in query.items():
        if str(value).isdigit():
            dokey.append(key)
    for edokey in dokey:
        newquery = copy.deepcopy(query)
        newquery[edokey] = int(newquery[edokey])-1
        rearray.append(newquery)
    return rearray

def printmsg(msg):
    ptime = time.strftime("%H:%M:%S", time.localtime())
    print('[ {} ] : {}'.format(ptime, msg))

#处理header头
def header_format(header):
    lst = header.split('\n')
    m = []
    for i in lst:
        if ':' in i:
            key = i.split(':')[0]
            value1 = i.split(':')[1]
            value = value1.lstrip()
            m.append([str(key), str(value)])
    return(dict(m))