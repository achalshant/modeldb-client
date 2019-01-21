# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import CommonService_pb2 as CommonService__pb2
from . import ExperimentService_pb2 as ExperimentService__pb2


class ExperimentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.createExperiment = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/createExperiment',
        request_serializer=ExperimentService__pb2.CreateExperiment.SerializeToString,
        response_deserializer=ExperimentService__pb2.CreateExperiment.Response.FromString,
        )
    self.updateExperimentNameOrDescription = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/updateExperimentNameOrDescription',
        request_serializer=ExperimentService__pb2.UpdateExperimentNameOrDescription.SerializeToString,
        response_deserializer=ExperimentService__pb2.UpdateExperimentNameOrDescription.Response.FromString,
        )
    self.addExperimentTags = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/addExperimentTags',
        request_serializer=ExperimentService__pb2.AddExperimentTags.SerializeToString,
        response_deserializer=ExperimentService__pb2.AddExperimentTags.Response.FromString,
        )
    self.deleteExperimentTags = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/deleteExperimentTags',
        request_serializer=ExperimentService__pb2.DeleteExperimentTags.SerializeToString,
        response_deserializer=ExperimentService__pb2.DeleteExperimentTags.Response.FromString,
        )
    self.addAttribute = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/addAttribute',
        request_serializer=CommonService__pb2.AddAttributes.SerializeToString,
        response_deserializer=CommonService__pb2.AddAttributes.Response.FromString,
        )
    self.getAttributes = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/getAttributes',
        request_serializer=CommonService__pb2.GetAttributes.SerializeToString,
        response_deserializer=CommonService__pb2.GetAttributes.Response.FromString,
        )
    self.getExperimentsInProject = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/getExperimentsInProject',
        request_serializer=ExperimentService__pb2.GetExperimentsInProject.SerializeToString,
        response_deserializer=ExperimentService__pb2.GetExperimentsInProject.Response.FromString,
        )
    self.getExperiment = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/getExperiment',
        request_serializer=ExperimentService__pb2.GetExperiment.SerializeToString,
        response_deserializer=ExperimentService__pb2.GetExperiment.Response.FromString,
        )
    self.deleteExperiment = channel.unary_unary(
        '/com.mitdbg.modeldb.ExperimentService/deleteExperiment',
        request_serializer=ExperimentService__pb2.DeleteExperiment.SerializeToString,
        response_deserializer=ExperimentService__pb2.DeleteExperiment.Response.FromString,
        )


class ExperimentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def createExperiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateExperimentNameOrDescription(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addExperimentTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperimentTags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addAttribute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentsInProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExperimentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'createExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.createExperiment,
          request_deserializer=ExperimentService__pb2.CreateExperiment.FromString,
          response_serializer=ExperimentService__pb2.CreateExperiment.Response.SerializeToString,
      ),
      'updateExperimentNameOrDescription': grpc.unary_unary_rpc_method_handler(
          servicer.updateExperimentNameOrDescription,
          request_deserializer=ExperimentService__pb2.UpdateExperimentNameOrDescription.FromString,
          response_serializer=ExperimentService__pb2.UpdateExperimentNameOrDescription.Response.SerializeToString,
      ),
      'addExperimentTags': grpc.unary_unary_rpc_method_handler(
          servicer.addExperimentTags,
          request_deserializer=ExperimentService__pb2.AddExperimentTags.FromString,
          response_serializer=ExperimentService__pb2.AddExperimentTags.Response.SerializeToString,
      ),
      'deleteExperimentTags': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperimentTags,
          request_deserializer=ExperimentService__pb2.DeleteExperimentTags.FromString,
          response_serializer=ExperimentService__pb2.DeleteExperimentTags.Response.SerializeToString,
      ),
      'addAttribute': grpc.unary_unary_rpc_method_handler(
          servicer.addAttribute,
          request_deserializer=CommonService__pb2.AddAttributes.FromString,
          response_serializer=CommonService__pb2.AddAttributes.Response.SerializeToString,
      ),
      'getAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.getAttributes,
          request_deserializer=CommonService__pb2.GetAttributes.FromString,
          response_serializer=CommonService__pb2.GetAttributes.Response.SerializeToString,
      ),
      'getExperimentsInProject': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentsInProject,
          request_deserializer=ExperimentService__pb2.GetExperimentsInProject.FromString,
          response_serializer=ExperimentService__pb2.GetExperimentsInProject.Response.SerializeToString,
      ),
      'getExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.getExperiment,
          request_deserializer=ExperimentService__pb2.GetExperiment.FromString,
          response_serializer=ExperimentService__pb2.GetExperiment.Response.SerializeToString,
      ),
      'deleteExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperiment,
          request_deserializer=ExperimentService__pb2.DeleteExperiment.FromString,
          response_serializer=ExperimentService__pb2.DeleteExperiment.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.mitdbg.modeldb.ExperimentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))