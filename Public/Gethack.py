# -*- coding: utf-8 -*-
from xml.dom.minidom import parse as ap
from urllib import parse as bp
from Public.Public import *


#读取XML文件,获取GET的全部请求
def GetreadXML(file):
    domTree = ap(file)
    rootNode = domTree.documentElement
    items = rootNode.getElementsByTagName("item")
    rearray = []
    for item in items:
        method = item.getElementsByTagName("method")[0]
        if method.childNodes[0].data == 'GET':
            date = []
            header = item.getElementsByTagName("request")[0]
            headerdata = header_format(header.childNodes[0].data)
            date.append(headerdata)
            url = item.getElementsByTagName("url")[0]
            date.append(changeGetMethod(url.childNodes[0].data))
            rearray.append(date)
    return rearray

#GET类型的url重新构造。
def changeGetMethod(url):
    allnewurl = []
    data = bp.urlparse(url)
    parsed_tuple = bp.parse_qs(data.query)
    for key,value in parsed_tuple.items():
        parsed_tuple[key] = value[0]
    redata = queryValue(parsed_tuple)
    for kvdata in redata:
        pkvdata = {}
        for key,value in kvdata.items():
            pkvdata[key] = value
        pkvdata = bp.urlencode(pkvdata)
        uupdata = [data.scheme,data.netloc,data.path,data.params,pkvdata,data.fragment]
        urlson = bp.urlunparse(uupdata)
        allnewurl.append(urlson)
    return allnewurl