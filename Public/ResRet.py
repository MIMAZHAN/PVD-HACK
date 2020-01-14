# -*- coding: utf-8 -*-
import requests


def GetReq(url,word,header=''):
    try:
        with requests.get(url, headers=header, timeout=5) as r:
            if word in r.text:
                return r.text
            else:
                return False
    except:
        print('Request Error : {}'.format(url))
        return False

def PostReq(url,data,word,header=''):
    try:
        with requests.post(url, headers=header, data=data, timeout=5) as r:
            if word in r.text:
                return r.text
            else:
                return False
    except:
        print('Request Error : {}'.format(url))
        return False
