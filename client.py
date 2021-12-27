# coding:utf-8

import grpc
import pymysql
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc


def run():
    conn = pymysql.connect(host='localhost', user='root', password='ICPC2021spring.', database='flask_books',
                           charset='utf8')
    cursor = conn.cursor()
    name = "data"
    try:
        sql = "INSERT INTO authors(name) VALUES (%s);"
        cursor.execute(sql, [name+'-guest'])
        conn.commit()
        result = {
            "retcode": "0",
            "retmsg": "success"
        }
    except Exception as e:
        conn.rollback()
        result = {
            "retcode": "201",
            "retmsg": "failure"
        }
    cursor.close()
    conn.close()
    conn = grpc.insecure_channel('127.0.0.1:5001')
    client = pb2_grpc.TestStub(channel=conn)
    response = client.Test01(pb2.Test01Req(
        name=name
    ))
    print(response.result)


if __name__ == '__main__':
    run()
