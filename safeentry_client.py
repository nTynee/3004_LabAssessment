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
            print(str(response.message))
            # TODO: if there's notification, show the message
            print("1) Login")
            print("2) Exit\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                self.login()
            elif user_input == '2':
                exit()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue
    
    def login(self):
        while(1):
            print('Please Enter Login Credentials.')
            nric = input("Enter NRIC: ")
            password = input("Enter Password: ")
            response = self.safe_entry_stub.Login(safeentry_pb2.UserInfo(nric = nric.upper(), password = password))

            if response.status == 'user':
                self.user_ui()
            elif response.status == 'officer':
                self.officer_ui()
            else:
                print('\nError Logging In. Please Try Again!\n')
                continue
    
    def user_ui(self):
        while(1):
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
            print("1) Individual Check In")
            print("2) Group Check In\n")
            print("3) Back\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                exit()
            elif user_input == '2':
                exit()
            elif user_input == '3':
                self.user_ui()
            else:
                print('\nInvalid! Please Try Again!\n')
                continue

    def check_out(self):
        exit()

    def show_history(self):
        response_history = self.location_stub.GetHistoryRecord(safeentry_pb2.get_user_history(nric = 'S9123456A'))    
        print('\n++++++++ HISTORY OF LOCATIONS ++++++++\n')
        print(str(response_history.response))
        exit()

    def declare_location(self):
        response_location = self.location_stub.DeclareLocation(safeentry_pb2.get_location_data(location = 'Hougang', nric = "S9123456A"))        
        print(str(response_location.response))
        exit()

if __name__ == '__main__':
    logging.basicConfig()
    client = SafeEntry()
    client.run()
