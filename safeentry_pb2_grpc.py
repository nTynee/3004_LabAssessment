# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import safeentry_pb2 as safeentry__pb2


class SafeEntryStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Message = channel.unary_unary(
                '/SafeEntry.SafeEntry/Message',
                request_serializer=safeentry__pb2.Request.SerializeToString,
                response_deserializer=safeentry__pb2.Reply.FromString,
                )
        self.Login = channel.unary_unary(
                '/SafeEntry.SafeEntry/Login',
                request_serializer=safeentry__pb2.UserInfo.SerializeToString,
                response_deserializer=safeentry__pb2.StatusInfo.FromString,
                )
        self.CheckIn = channel.unary_unary(
                '/SafeEntry.SafeEntry/CheckIn',
                request_serializer=safeentry__pb2.CheckRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckResponse.FromString,
                )
        self.CheckOut = channel.unary_unary(
                '/SafeEntry.SafeEntry/CheckOut',
                request_serializer=safeentry__pb2.CheckRequest.SerializeToString,
                response_deserializer=safeentry__pb2.CheckResponse.FromString,
                )
        self.Check = channel.unary_unary(
                '/SafeEntry.SafeEntry/Check',
                request_serializer=safeentry__pb2.StatusInfo.SerializeToString,
                response_deserializer=safeentry__pb2.StatusResponse.FromString,
                )


class SafeEntryServicer(object):
    """The greeting service definition.
    """

    def Message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SafeEntryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Message': grpc.unary_unary_rpc_method_handler(
                    servicer.Message,
                    request_deserializer=safeentry__pb2.Request.FromString,
                    response_serializer=safeentry__pb2.Reply.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=safeentry__pb2.UserInfo.FromString,
                    response_serializer=safeentry__pb2.StatusInfo.SerializeToString,
            ),
            'CheckIn': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIn,
                    request_deserializer=safeentry__pb2.CheckRequest.FromString,
                    response_serializer=safeentry__pb2.CheckResponse.SerializeToString,
            ),
            'CheckOut': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckOut,
                    request_deserializer=safeentry__pb2.CheckRequest.FromString,
                    response_serializer=safeentry__pb2.CheckResponse.SerializeToString,
            ),
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=safeentry__pb2.StatusInfo.FromString,
                    response_serializer=safeentry__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry.SafeEntry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SafeEntry(object):
    """The greeting service definition.
    """

    @staticmethod
    def Message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Message',
            safeentry__pb2.Request.SerializeToString,
            safeentry__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Login',
            safeentry__pb2.UserInfo.SerializeToString,
            safeentry__pb2.StatusInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/CheckIn',
            safeentry__pb2.CheckRequest.SerializeToString,
            safeentry__pb2.CheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/CheckOut',
            safeentry__pb2.CheckRequest.SerializeToString,
            safeentry__pb2.CheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.SafeEntry/Check',
            safeentry__pb2.StatusInfo.SerializeToString,
            safeentry__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class LocationDataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeclareLocation = channel.unary_unary(
                '/SafeEntry.LocationData/DeclareLocation',
                request_serializer=safeentry__pb2.get_location_data.SerializeToString,
                response_deserializer=safeentry__pb2.location.FromString,
                )
        self.GetHistoryRecord = channel.unary_unary(
                '/SafeEntry.LocationData/GetHistoryRecord',
                request_serializer=safeentry__pb2.get_user_history.SerializeToString,
                response_deserializer=safeentry__pb2.history_record.FromString,
                )


class LocationDataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeclareLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHistoryRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocationDataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeclareLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.DeclareLocation,
                    request_deserializer=safeentry__pb2.get_location_data.FromString,
                    response_serializer=safeentry__pb2.location.SerializeToString,
            ),
            'GetHistoryRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHistoryRecord,
                    request_deserializer=safeentry__pb2.get_user_history.FromString,
                    response_serializer=safeentry__pb2.history_record.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry.LocationData', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocationData(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeclareLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.LocationData/DeclareLocation',
            safeentry__pb2.get_location_data.SerializeToString,
            safeentry__pb2.location.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHistoryRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.LocationData/GetHistoryRecord',
            safeentry__pb2.get_user_history.SerializeToString,
            safeentry__pb2.history_record.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NotificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendNotification = channel.unary_unary(
                '/SafeEntry.Notification/SendNotification',
                request_serializer=safeentry__pb2.get_notification.SerializeToString,
                response_deserializer=safeentry__pb2.noti_info.FromString,
                )


class NotificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SendNotification,
                    request_deserializer=safeentry__pb2.get_notification.FromString,
                    response_serializer=safeentry__pb2.noti_info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SafeEntry.Notification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Notification(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SafeEntry.Notification/SendNotification',
            safeentry__pb2.get_notification.SerializeToString,
            safeentry__pb2.noti_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
