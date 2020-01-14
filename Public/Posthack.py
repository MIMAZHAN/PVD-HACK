# -*- coding: utf-8 -*-
from xml.dom.minidom import parse as ap
from urllib import parse as bp
from Public.Public import *
import json


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except:
        return False
    return json_object

def post_header_format(header):
    lst = header.split('\n')
    m = []
    for i in lst:
        if ':' in i:
            key = i.split(':')[0]
            value1 = i.split(':')[1]
            value = value1.lstrip()
            m.append([str(key), str(value)])
    m = dict(m)
    m['postfinallydata'] = lst[len(lst)-1]
    return(m)

#读取XML文件,获取POST的全部请求
def PostreadXML(file):
    domTree = ap(file)
    rootNode = domTree.documentElement
    items = rootNode.getElementsByTagName("item")
    rearray = []
    for item in items:
        everydata = []
        method = item.getElementsByTagName("method")[0]
        if method.childNodes[0].data == 'POST':
            date = []
            header = item.getElementsByTagName("request")[0]
            headerdata = post_header_format(header.childNodes[0].data)
            url = item.getElementsByTagName("url")[0]
            posturl = url.childNodes[0].data
            date.append(posturl)
            postdata = headerdata['postfinallydata']
            date.append(changePostMethod(postdata))
            headerdata.pop('postfinallydata')
            date.append(headerdata)
        if len(date) > 0:
            rearray.append(date)
    if len(rearray)>0:
        return rearray
    else:
        return False

def changePostMethod(data):
    if is_json(data):
        rejsondata = []
        Alljsondata = queryValue(json.loads(data))
        for changejson in Alljsondata:
            rejsondata.append(json.dumps(changejson))
        return rejsondata
    elif '=' in data:
        data = bp.parse_qs(data)
        for key,value in data.items():
            data[key] = value[0]
        return queryValue(data)
    else:
        return False