#coding=utf-8
"""
Create On 2017/3/22

@author: Ron2
"""


import hashlib


def calcHash(data):
    """
    计算data的hash值
    :param data:
    :return:            E.g
    """
    shaObj = hashlib.sha256()
    shaObj.update(data)
    return shaObj.hexdigest()


maxLogNum = 0
def createLogNum(clientId):
    """
    生成一个新的LogNum
    :param clientId:                当前的客户端表示
    :return:
    """
    global maxLogNum

    ''' 忽略clientId部分，先递增 '''
    logNum = maxLogNum / (10 ** len(str(clientId))) + 1

    ''' 添加clientId部分 '''
    newMaxLogNum = logNum * (10 ** len(str(clientId))) + clientId
    maxLogNum = newMaxLogNum
    return newMaxLogNum


if __name__ == "__main__":
    print createLogNum(1001)
    print createLogNum(1001)
    print createLogNum(1001)
    print createLogNum(1001)
    print createLogNum(1001)
