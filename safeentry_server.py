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
from re import I
import re

import grpc
from numpy import diff
import safeentry_pb2
import safeentry_pb2_grpc

import json
import os
import pandas as pd
from csv import writer
from datetime import datetime

input_file = ""
client_list = []
notification_list = []

class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):
    print("+++++++++++++++++++++++++ SafeEntry System Server Started +++++++++++++++++++++++++")

    def Message(self, request, context):
        return safeentry_pb2.Reply(message = request.message)

    def Login(self, request, context):
        if request.role == 1:
            with open("Users/Users.json", 'r') as f:
                data = json.load(f) 
            for i in data:
                if (request.nric == i['nric'] and request.password == i['password']):
                    print("User {} ({}) has successfully logged in.".format(i['name'], i['nric']))
                    return safeentry_pb2.StatusInfo(status = 'success', name = i['name'])

        elif request.role == 2:
            with open("Officers/Officers.json", 'r') as f:
                data = json.load(f) 
            for i in data:
                if (request.nric.lower() == i['email'] and request.password == i['password']):
                    print("MOH officer {} ({}) has successfully logged in.".format(i['name'], i['email']))
                    return safeentry_pb2.StatusInfo(status = 'success', name = i['name'])  

        print("User has error logging in.")
        return safeentry_pb2.StatusInfo(status = 'error')
    
    def CheckIn(self, request, context):

        location_path = "Locations/" + request.location + ".json"  
        with open(location_path, 'r') as f:
            data = json.load(f)  
        
        if len(request.nric) > 1:
            # store into location data
            for i in request.nric:
                dict = {
                    "ic" : i,
                    "checkin" : request.datetime,
                    "checkout" : ""
                }    
                data.insert(0, dict)
                with open(location_path, 'w') as f:
                    json.dump(data, f)

                # store into user history
                user_path = "Records/" + i + ".json" 
                with open(user_path, 'r') as f:
                    user_data = json.load(f)  
                dict2 = {
                    "location" : request.location,
                    "checkin" : request.datetime,
                    "checkout" : ""
                }
                user_data.insert(0, dict2)
                with open(user_path, 'w') as f:
                    json.dump(user_data, f)

        else:
            dict = {
                    "ic" : request.nric[0],
                    "checkin" : request.datetime,
                    "checkout" : ""
                }    
            data.insert(0, dict)

            # print(data)

            with open(location_path, 'w') as f:
                json.dump(data, f)

            # store into user history
            user_path = "Records/" + request.nric[0] + ".json" 
            with open(user_path, 'r') as f:
                user_data = json.load(f)  
            dict2 = {
                "location" : request.location,
                "checkin" : request.datetime,
                "checkout" : ""
            }
            user_data.insert(0, dict2)
            with open(user_path, 'w') as f:
                json.dump(user_data, f)

        check_bool = True
        
        if check_bool:
            for i in request.nric: 
                print('{} has successfully checked in at {} during {}.'.format(i, request.location, request.datetime))
        return safeentry_pb2.CheckResponse(status = check_bool)

    def CheckOut(self, request, context):
        with open("Locations/" + request.location + ".json") as f:
            data = json.load(f)

        if len(request.nric) > 1:
            for x in request.nric:
                # store into user history
                with open("Records/" + x + ".json") as f:
                    user_data = json.load(f)
                for i in user_data:
                    if i['location'] == request.location:
                        i['checkout'] = request.datetime
                        break
                with open("Records/" + x + ".json", 'w') as f:
                    json.dump(user_data, f)

                # store into location data
                for i in data:
                    if i["ic"] == x:
                        i["checkout"] = request.datetime
                        print('{} has successfully checked out at {} during {}.'.format(x, request.location, request.datetime))
                        break
        else:
            # store into user history
            with open("Records/" + request.nric[0] + ".json") as f:
                    user_data = json.load(f)
            for i in user_data:
                if i['location'] == request.location:                    
                    i['checkout'] = request.datetime
                    break
            with open("Records/" + request.nric[0] + ".json", 'w') as f:
                json.dump(user_data, f)

            # store into location data
            for i in data:
                if i["ic"] == request.nric[0]:
                    i["checkout"] = request.datetime                    
                    break

        with open("Locations/" + request.location + ".json", 'w') as f:
            json.dump(data, f)
            print('{} has successfully checked out at {} during {}.'.format(request.nric[0], request.location, request.datetime))
        
        check_bool = True
 
        return safeentry_pb2.CheckResponse(status = check_bool)


class Location(safeentry_pb2_grpc.LocationDataServicer):

    def GetHistoryRecord(self, request, context):
        print("Retrieving history records of user {}...".format(request.nric))

        path = "Records/" + request.nric + ".json"
        if os.path.exists(path):    
            with open(path, 'r') as f:
                data = json.load(f)      
            return safeentry_pb2.history_record(response=data, status='success')   

        return safeentry_pb2.history_record(response=None, status='error')    

    def DeclareLocation(self, request, context):
        global notification_list
        print("Retrieving location details for declaration...")

        infected_checkin = datetime.strptime(request.datetime, '%Y-%m-%dT%H:%M:%S.%f')

        # people within the range of 14 days
        with open("Locations/" + request.location + ".json", 'r') as f:
            location_data = json.load(f) 

        with open("Users/Users.json", 'r') as f:
            user_data = json.load(f) 

        for i in location_data:
            checkin = datetime.strptime(i["checkin"], '%Y-%m-%dT%H:%M:%S.%f')  
            checkout = i["checkout"]
            if checkout != "":
                checkout = datetime.strptime(checkout, '%Y-%m-%dT%H:%M:%S.%f') 
                checkout = checkout.strftime('%d/%m/%y %H:%M:%S')  
            else:
                checkout = "NA"                
            difference = (infected_checkin - checkin).days

            if difference <= 14 and difference >= -14:
                #write to csv 
                data = []
                for j in user_data: 
                    if i['ic'] == j['nric']:
                        #save to a global list to return back
                        notification_list.append(i["ic"])         
                        location = re.sub(r"(\w)([A-Z])", r"\1 \2", request.location)             
                        data = pd.DataFrame({'Content': ["Hi {0}, there's a COVID case while you were at {1} from {2} to {3}. Please take note for 14 days!".format(j['name'], location, checkin.strftime('%d/%m/%y %H:%M:%S'), checkout)]})

                        #check exists
                        path = "Notification/" + i['ic'] + ".csv"
                        exist = os.path.isfile(path)    
                        if exist:
                            df = pd.read_csv(path)
                            df = pd.concat([df, data]).drop_duplicates()
                            df.to_csv(path, mode='w', index=False, header=['Content'])
                        else:                            
                            data.to_csv(path, mode='w', index=False, header=['Content'])
                            
                        break

        
        #drop duplicates
        temp_list = list(dict.fromkeys(notification_list))    
        print("Declaring location for {}...".format(temp_list))
        return safeentry_pb2.location(response='success', noti_list=notification_list)


class Password(safeentry_pb2_grpc.PaswordSettingServicer):

    def ChangePassword(self, request, context):
        print("Retrieving password details...")

        with open("Users/Users.json", 'r') as f:
            data = json.load(f)     

        for i in data:        
            if request.nric == i['nric']:
                if request.old_password == i['password'] and request.new_password != i['password']:
                    i['password'] = request.new_password
                    with open("Users/Users.json", 'w') as f:
                        json.dump(data, f)            
                    return safeentry_pb2.password(response="success")   
                elif request.new_password == i['password']:
                    return safeentry_pb2.password(response="error1")
        return safeentry_pb2.password(response="error2")


class Notification(safeentry_pb2_grpc.NotificationServicer):

    def __init__(self):
        # notification string
        self.notification = ''

    # the stream which will be used to send new notifications to clients
    def SendNotification(self, request_iterator, context):
        """
        This is a response-stream type call. This means the server can keep sending messages.
        Every client opens this connection and waits for server to send new messages.
        """
        previous_notification = ''
        # for every client a infinite loop starts (in gRPC's own managed thread)
        while True:
            if self.notification != previous_notification:
                previous_notification = self.notification
                yield self.notification
    
    def ReceiveDeclaration(self, request: safeentry_pb2.DeclarationInfo, context):
        """
        This method is called when a clients sends a Declaration to the server.
        """
        self.notification = request
        return safeentry_pb2.Empty()

    def DeleteUserFromNotiList(self, request, context):
        for x in notification_list:
            if x == request.message:
                notification_list.remove(request.message)
        return safeentry_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    safeentry_pb2_grpc.add_LocationDataServicer_to_server(Location(), server)
    safeentry_pb2_grpc.add_NotificationServicer_to_server(Notification(), server)
    safeentry_pb2_grpc.add_PaswordSettingServicer_to_server(Password(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()    
    serve()
