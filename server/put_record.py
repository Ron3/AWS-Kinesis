#coding=utf-8
"""
Create On 2017/3/22

@author: Ron2
"""


import boto3
import time
import conf
import common
import datetime
import base64
import getpass


def putRecord_random_shard(data):
    """
    将数据随机写入到shard
    :param data:
    :return:
    """

    streamObj = boto3.client("kinesis")
    responseDic = streamObj.put_record(
        StreamName=conf.STREAM_NAME,
        Data=data,
        PartitionKey=common.calcHash(data)
        # ExplicitHashKey=''
        # SequenceNumberForOrdering='string'
    )

    print responseDic


if __name__ == "__main__":
    putRecord_random_shard("test9")