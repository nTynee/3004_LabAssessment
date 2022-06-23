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
from numpy import diff
import safeentry_pb2
import safeentry_pb2_grpc

import json
from datetime import datetime

input_file = ""

class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):

    def Message(self, request, context):
        return safeentry_pb2.Reply(message = request.message)

    def Login(self, request, context):
        if request.role == 1:
            with open("Users.json", 'r') as f:
                data = json.load(f) 
            for i in data:
                if (request.nric == i['nric'] and request.password == i['password']):
                    return safeentry_pb2.StatusInfo(status = 'success')
                else:
                    print("error")
                    return safeentry_pb2.StatusInfo(status = 'error')

        elif request.role == 2:
            with open("Officers.json", 'r') as f:
                data = json.load(f) 
            for i in data:
                if (request.nric.lower() == i['email'] and request.password == i['password']):
                    return safeentry_pb2.StatusInfo(status = 'success')  
                else:
                    print("error")
                    return safeentry_pb2.StatusInfo(status = 'error')
    
    def CheckIn(self, request, context):
        dict = {
            "ic" : request.nric,
            "checkin" : request.datetime,
            "checkout" : "",
            "infected" : "F"
        }
        with open("Locations/" + request.location + ".json") as f:
            data = json.load(f)

        data.append(dict)

        with open("Locations/" + request.location + ".json", 'w') as f:
            json.dump(data, f)
            check_bool = True
        
        if check_bool:
            print(request.nric + ' has successfully checked in at ' + request.location + ' during ' + request.datetime)
        return safeentry_pb2.CheckResponse(status = check_bool)

    def CheckOut(self, request, context):
        dict = {
            "ic" : request.nric,
            "checkin" : request.datetime,
            "checkout" : "",
            "infected" : "F"
        }
        with open("Locations/" + request.location + ".json") as f:
            data = json.load(f)

        for i in data:
            if i["ic"] == request.nric:
                i["checkout"] = request.datetime
                break

        with open("Locations/" + request.location + ".json", 'w') as f:
            json.dump(data, f)
            check_bool = True

        if check_bool:
            print(request.nric + ' has successfully checked out at ' + request.location + ' during ' + request.datetime)
        return safeentry_pb2.CheckResponse(status = check_bool)

    def Check(self, request, context):
        # TODO
        pass



class Location(safeentry_pb2_grpc.LocationDataServicer):

    def GetHistoryRecord(self, request, context):
        print("Retrieving history records...")
        print(request.nric)
        with open(request.nric + ".json", 'r') as f:
            data = json.load(f)      
        return safeentry_pb2.history_record(response=data)    

    def DeclareLocation(self, request, context):
        print("Retrieving location details...")

        # set user as covid infected
        with open("Locations/" + request.location + ".json", 'r') as f:
            data = json.load(f) 

        for i in data:
            if i["ic"] == request.nric:
                i["infected"] = 'T'
                infected_checkin = datetime.strptime(i["checkin"], '%Y-%m-%dT%H:%M:%S.%f')

        with open("Locations/" + request.location + ".json", "w") as f:
            json.dump(data, f)
        
        # people within the range of 14 days
        noti_list = []
        for i in data:
            checkin = datetime.strptime(i["checkin"], '%Y-%m-%dT%H:%M:%S.%f')                   
            difference = (infected_checkin - checkin).days

            if difference <= 14 and difference >= -14:
                #save to a list to return back
                noti_list.append(i["ic"])
        
        print("Declaring location...")
        return safeentry_pb2.location(response=noti_list)


class Notification(safeentry_pb2_grpc.NotificationServicer):

    def SendNotification(self, request, context):
        return safeentry_pb2.noti_info(response="testtttt")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    safeentry_pb2_grpc.add_LocationDataServicer_to_server(Location(), server)
    safeentry_pb2_grpc.add_NotificationServicer_to_server(Notification(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()    
    serve()
