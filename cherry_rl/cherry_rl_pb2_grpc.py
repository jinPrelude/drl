# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cherry_rl_pb2 as cherry__rl__pb2


class CherryRLStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DiscreteGymStep = channel.unary_unary(
                '/CherryRL/DiscreteGymStep',
                request_serializer=cherry__rl__pb2.CallRequest.SerializeToString,
                response_deserializer=cherry__rl__pb2.DiscreteGymReply.FromString,
                )


class CherryRLServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DiscreteGymStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CherryRLServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DiscreteGymStep': grpc.unary_unary_rpc_method_handler(
                    servicer.DiscreteGymStep,
                    request_deserializer=cherry__rl__pb2.CallRequest.FromString,
                    response_serializer=cherry__rl__pb2.DiscreteGymReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CherryRL', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CherryRL(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DiscreteGymStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CherryRL/DiscreteGymStep',
            cherry__rl__pb2.CallRequest.SerializeToString,
            cherry__rl__pb2.DiscreteGymReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)