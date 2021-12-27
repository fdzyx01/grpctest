# coding:utf-8

import time
import grpc
import pymysql
import test_pb2 as pb2
import test_pb2_grpc as pb2_grpc

from concurrent import futures


class Test(pb2_grpc.TestServicer):
    def Test01(self, request, context):
        name = request.name + "-host"

        conn = pymysql.connect(host='localhost', user='root', password='ICPC2021spring.', database='flask_books',
                               charset='utf8')
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO authors(name) VALUES (%s);"
            cursor.execute(sql, [name])
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

        return pb2.Test01Reply(result=result)


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    #注册
    pb2_grpc.add_TestServicer_to_server(Test(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5001')
    print('server will start at 0.0.0.0:5001')
    grpc_server.start()
    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
