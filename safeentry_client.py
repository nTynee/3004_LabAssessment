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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

import time
import os

NRIC = ''
LOCATIONS = [] 

class SafeEntry: 
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')
        self.safe_entry_stub = safeentry_pb2_grpc.SafeEntryStub(self.channel)
        self.location_stub = safeentry_pb2_grpc.LocationDataStub(self.channel)
        
    def run(self):
        # NOTE(gRPC Python Team): .close() is possible on a channel and should be
        # used in circumstances in which the with statement does not fit the needs
        # of the code.
        response = self.safe_entry_stub.Message(safeentry_pb2.Request(message = 'Hello! Welcome to the SafeEntry system!'))

        while(1):
            # get locations from folder
            self.store_locations()

            # print login ui
            print(str(response.message))
            print("1) User Login")
            print("2) Officer Login")
            print("3) Exit\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                self.login(1)
            if user_input == '2':
                self.login(2)
            elif user_input == '3':
                exit()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue
    
    def login(self, number):
        global NRIC
        while(1):
            print('Please Enter Login Credentials.')
            nric = input("Enter NRIC: ")
            password = input("Enter Password: ")
            response = self.safe_entry_stub.Login(safeentry_pb2.UserInfo(nric = nric.upper(), password = password))

            NRIC = nric.upper()

            if response.status == 'success':
                if number == 1:
                    self.user_ui()
                elif number == 2:
                    self.officer_ui()
            else:
                print('\nError Logging In. Please Try Again!\n')
                continue
    
    def user_ui(self):
        while(1):
            # TODO: if there's notification, show the message
            print("\nWelcome!\n")
            print("1) Check In")
            print("2) Check Out")
            print("3) Show History")
            print("4) Exit\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                self.check_in()
            elif user_input == '2':
                self.check_out()
            elif user_input == '3':
                self.show_history()
            elif user_input == '4':
                exit()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue

    def officer_ui(self):
        while(1):
            print("1) Declare Location")
            print("2) Exit\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                self.declare_location()
            elif user_input == '2':
                exit()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue

    def check_in(self):
        while(1):
            print('\n++++++++ CHECKING IN ++++++++\n')
            print("1) Individual Check In")
            print("2) Group Check In")
            print("3) Back\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                print("List Of Locations: ")
                self.print_locations()

                location_input = input("\nPlease Select Location: ")
                
                if location_input.isdigit() or int(location_input) <= LOCATIONS.count:
                    date_time = time.strftime("%d/%m/%Y %H:%M:%S")
                    response = self.safe_entry_stub.CheckIn(safeentry_pb2.CheckRequest(nric = NRIC, location = LOCATIONS[int(location_input)-1], datetime = date_time))

                    if response is True:
                        print('Successfully checked in at ' + LOCATIONS[int(location_input)-1] + ' during ' + date_time)
                        self.user_ui()
                    else:
                        print('Error! Please Check In Again!\n')
                        self.check_in()
                else:
                    print('\nInvalid Input! Please Try Again!\n')
                    continue

            elif user_input == '2':
                exit()
            elif user_input == '3':
                self.user_ui()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue

    def check_out(self):
        while(1):
            print('\n++++++++ CHECKING OUT ++++++++\n')
            print("List Of Locations: ")
            self.print_locations()

            location_input = input("\nPlease Select Location: ")
            
            if location_input.isdigit() or int(location_input) <= LOCATIONS.count:
                date_time = time.strftime("%d/%m/%Y %H:%M:%S")
                response = self.safe_entry_stub.CheckOut(safeentry_pb2.CheckRequest(nric = NRIC, location = LOCATIONS[int(location_input)-1], datetime = date_time))

                if response is True:
                    print('Successfully checked out at ' + LOCATIONS[int(location_input)-1] + ' during ' + date_time)
                    self.user_ui()
                else:
                    print('Error! Please Check Out Again!\n')
                    self.check_out()
            else:
                print('\nInvalid Input! Please Try Again!\n')
                continue

    def store_locations(self):
        for x in os.listdir('Locations'):
            if x.endswith(".json"):
                LOCATIONS.append(x.replace('.json', ''))

    def print_locations(self):
        i = 1
        for x in LOCATIONS:
            print(str(i) + ') ' + x)
            i+=1

    def show_history(self):
        response_history = self.location_stub.GetHistoryRecord(safeentry_pb2.get_user_history(nric = NRIC))    
        print('\n++++++++ HISTORY OF LOCATIONS ++++++++\n')
        print(str(response_history.response))
        exit()

    def declare_location(self):
        while(1):
            print("List Of Locations: ")
            self.print_locations()

            location_input = input("\nPlease Select Location: ")
            if location_input.strip().isdigit() or int(location_input) <= LOCATIONS.count:
                response_location = self.location_stub.DeclareLocation(safeentry_pb2.get_location_data(location = LOCATIONS[int(location_input)-1], nric = "S9123456A"))        
                print(str(response_location.response))
                self.officer_ui()
            else:
                print('\nInvalid Input! Please Try Again!\n')
                continue

if __name__ == '__main__':
    logging.basicConfig()
    client = SafeEntry()
    client.run()
