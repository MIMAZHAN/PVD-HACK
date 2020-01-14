from Public.Public import *
from Public.Gethack import *
from Public.ResRet import *
from Public.Posthack import *
import argparse


def head():
    print('''
    -----
    |
        Permission defect vulnerability
        PDV - Vulnerability detection
        -w WORD -f FILE
                                            |
                                         -----
    ''')

def userinput():
    parser = argparse.ArgumentParser(description='PDV')
    parser.add_argument("-w", help="差异字符", required=True)
    parser.add_argument("-f", help="burp xml file", required=True)
    args = parser.parse_args()
    return args

def Getcheck(date,word):
    for item in date:
        if len(item[1]) > 0:
            for url in item[1]:
                if GetReq(url,word,header=item[0]):
                    printmsg('Congratulations! url : {} Loopholes (yes headers)'.format(url))
                if GetReq(url,word):
                    printmsg('Congratulations! url : {} Loopholes (no headers)'.format(url))

def Postcheck(date,word):
    for item in date:
        if len(item[1]) > 0:
            for date in item[1]:
                if PostReq(item[0],date,word,header=item[2]):
                    printmsg('Congratulations! url : {} Loopholes (yes headers)'.format(item[0]))
                    printmsg('request date: {}'.format(date))
                if PostReq(item[0],date,word):
                    printmsg('Congratulations! url : {} Loopholes (no headers)'.format(item[0]))
                    printmsg('request date: {}'.format(date))

if __name__ == "__main__":
    head()
    args = userinput()
    word = args.w
    date = GetreadXML(args.f)
    Getcheck(date,word)
    date = PostreadXML(args.f)
    Postcheck(date,word)
    printmsg('All items tested! If there is a vulnerability, it will output.')