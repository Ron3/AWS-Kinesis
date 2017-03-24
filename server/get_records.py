#coding=utf-8
"""
Create On 2017/3/22

@author: Ron2
"""


import conf
import boto3


def getRecords():
    """
    从Kinesis中读取数据
    :return:
    """
    # ''' 接着读回来 '''
    streamObj = boto3.client("kinesis")
    responseDic = streamObj.get_shard_iterator(StreamName=conf.STREAM_NAME,
                                               ShardId="shardId-000000000000",
                                               ShardIteratorType="AT_SEQUENCE_NUMBER",
                                               StartingSequenceNumber="49571577983902154079750021346295642001813134799326412802",

                                               # ShardIteratorType="TRIM_HORIZON",
                                               # StartingSequenceNumber="0",
                                               # Timestamp=datetime.datetime.now()
                                               )

    print "get shard iterator success"
    shardIterator = responseDic.get("ShardIterator")

    responseDic = streamObj.get_records(ShardIterator=shardIterator, Limit=1)
    print "responseDic==> ", responseDic


if __name__ == "__main__":
    getRecords()


