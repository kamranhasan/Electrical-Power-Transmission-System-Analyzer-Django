# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/longrunning/operations.proto
from google.longrunning.operations_proto_pb2 import *
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class OperationsStub(object):
    """Manages long-running operations with an API service.

  When an API method normally takes long time to complete, it can be designed
  to return [Operation][google.longrunning.Operation] to the client, and the client can use this
  interface to receive the real response asynchronously by polling the
  operation resource, or pass the operation resource to another API (such as
  Google Cloud Pub/Sub API) to receive the response.  Any API service that
  returns long-running operations should implement the `Operations` interface
  so developers can have a consistent client experience.
  """

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.GetOperation = channel.unary_unary(
            "/google.longrunning.Operations/GetOperation",
            request_serializer=GetOperationRequest.SerializeToString,
            response_deserializer=Operation.FromString,
        )
        self.ListOperations = channel.unary_unary(
            "/google.longrunning.Operations/ListOperations",
            request_serializer=ListOperationsRequest.SerializeToString,
            response_deserializer=ListOperationsResponse.FromString,
        )
        self.CancelOperation = channel.unary_unary(
            "/google.longrunning.Operations/CancelOperation",
            request_serializer=CancelOperationRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.DeleteOperation = channel.unary_unary(
            "/google.longrunning.Operations/DeleteOperation",
            request_serializer=DeleteOperationRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
