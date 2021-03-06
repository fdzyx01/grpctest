# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import test_pb2 as test__pb2


class TestStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Test01 = channel.unary_unary(
        '/test.Test/Test01',
        request_serializer=test__pb2.Test01Req.SerializeToString,
        response_deserializer=test__pb2.Test01Reply.FromString,
        )


class TestServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Test01(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TestServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Test01': grpc.unary_unary_rpc_method_handler(
          servicer.Test01,
          request_deserializer=test__pb2.Test01Req.FromString,
          response_serializer=test__pb2.Test01Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'test.Test', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
