#coding=utf-8
"""
Create On 2017/3/22

@author: Ron2
"""

import boto3
import json
import datetime
import conf

Encoder = json.JSONEncoder()
Decoder = json.JSONDecoder()


def descStream():
    """
    得到这个流当前的情况
    :param data:
    :return:
    """
    streamObj = boto3.client("kinesis")
    responseDic = streamObj.describe_stream(StreamName=conf.STREAM_NAME)
    descDic = responseDic.get("StreamDescription")

    class DescEncoder(json.JSONEncoder):
        """
        """
        def default(self, obj):
            """
            :param obj:
            :return:
            """
            if isinstance(obj, datetime.datetime):
                return str(obj)

            return json.JSONEncoder.default(self, obj)

    print json.dumps(descDic, cls=DescEncoder)

    # 将会得到这样的一串数据
    # {
    #     "HasMoreShards": false,
    #     "RetentionPeriodHours": 24,
    #     "StreamName": "MyStream",
    #     "Shards": [
    #         {
    #             "ShardId": "shardId-000000000000",
    #             "HashKeyRange": {
    #                 "EndingHashKey": "340282366920938463463374607431768211455",
    #                 "StartingHashKey": "0"
    #             },
    #             "SequenceNumberRange": {
    #                 "StartingSequenceNumber": "49571568732482609959687117931971140088870254941080387586"
    #             }
    #         }
    #     ],
    #     "StreamARN": "arn:aws:kinesis:ap-southeast-1:xxxx:stream/MyStream",
    #     "EnhancedMonitoring": [
    #         {
    #             "ShardLevelMetrics": []
    #         }
    #     ],
    #     "StreamCreationTimestamp": "2017-03-22 16:53:29+08:00",
    #     "StreamStatus": "ACTIVE"
    # }





if __name__ == "__main__":
    descStream()






