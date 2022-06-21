# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

import json
from google.protobuf.json_format import Parse

input_file = ""

class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):

    def Message(self, request, context):
        return safeentry_pb2.Reply(message = request.message)
    
    def Check(self, request, context):
        # TODO
        pass



class Location(safeentry_pb2_grpc.LocationDataServicer):

    def GetLocation(self, request, context):
        print("Retrieving location details...")
        print(request.location)
        with open(request.location + ".json", 'r') as f:
            data = json.load(f)       
        return safeentry_pb2.location(response=data)    

    def DeclareLocation(self, request, context):
                print("Declaring location...")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    safeentry_pb2_grpc.add_LocationDataServicer_to_server(Location(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()    
    serve()
