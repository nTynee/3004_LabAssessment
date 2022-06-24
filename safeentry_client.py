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
from cgi import test
import csv

import logging
import sys
import time

import grpc
from nbformat import read
from numpy import empty
import safeentry_pb2
import safeentry_pb2_grpc

import re
from datetime import date, datetime
import threading
import os

NRIC = ''
LOCATIONS = []
NOTIFICATIONS = []

class SafeEntry: 
    def __init__(self) -> None:
        self.channel = grpc.insecure_channel('localhost:50051')
        self.safe_entry_stub = safeentry_pb2_grpc.SafeEntryStub(self.channel)
        self.location_stub = safeentry_pb2_grpc.LocationDataStub(self.channel)
        self.notification_stub = safeentry_pb2_grpc.NotificationStub(self.channel)
        self.password_stub = safeentry_pb2_grpc.PaswordSettingStub(self.channel)

        # create new listening thread for when new message streams come in
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        """
        This method will be ran in a separate thread as the main/ui thread, because the for-in call is blocking
        when waiting for new messages
        """
        global NOTIFICATIONS
        for notification in self.notification_stub.SendNotification(safeentry_pb2.Empty()):  # this line will wait for new messages from the server!
            #print(notification.message)
            if NRIC != '':
                if NRIC in notification.message:
                    #print("aaaaa")
                    file = 'Notification/' + NRIC + '.csv'
        
                    with open(file, 'r', encoding='UTF8') as f:
                        reader = list(csv.reader(f))
                        if NOTIFICATIONS != reader:
                            # print(NOTIFICATIONS)
                            # print(reader)
                            difference = len(reader) - len(NOTIFICATIONS)
                            temp_list = []
                            for i in range(difference):
                                NOTIFICATIONS.append(reader[-i])
                                temp_list.append(reader[-i])

                            # prints new notifications
                            print("\n+++++++++++++++++++++ NEW NOTIFICATION +++++++++++++++++++++")
                            for x in temp_list:
                                print (x)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                            temp_list.clear()

                            # send request to server to delete user nric from server's notification list
                            self.notification_stub.DeleteUserFromNotiList(safeentry_pb2.Request(message = NRIC))
                
        
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
                self.login(1, "NRIC")
            if user_input == '2':
                self.login(2, "Email")
            elif user_input == '3':
                exit()
            else:
                print("\nInvalid! Please Try Again!\n")
                continue
    
    def login(self, number, word):
        global NRIC
        while(1):
            print("Please Enter Login Credentials.")
            nric = input("Enter {}: ".format(word))
            password = input("Enter Password: ")
            response = self.safe_entry_stub.Login(safeentry_pb2.UserInfo(nric = nric.upper(), password = password, role = number))

            NRIC = nric.upper()

            if response.status == 'success':
                if number == 1:
                    self.user_ui()
                elif number == 2:
                    self.officer_ui()
            else:
                print("\nError Logging In. Please Try Again!\n")
                continue
    
    def user_ui(self):
        while(1):
            print("\nWelcome!")
            # get notifications from folder
            bool = self.store_notifications()
            # print notifications from folder
            self.check_notifications(bool)
            print("1) Check In")
            print("2) Check Out")
            print("3) Show History")
            print("4) Change Password")
            print("5) Exit\n")
            user_input = input("Please Select Choice: ")

            if user_input == '1':
                self.check_in()
            elif user_input == '2':
                self.check_out()
            elif user_input == '3':
                self.show_history()
            elif user_input == '4':
                self.change_password()
                exit()
            elif user_input == '5':
                exit()
            else:
                print("\nInvalid! Please Try Again!\n")
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
                print("\nInvalid! Please Try Again!\n")
                continue

    def store_notifications(self):
        file = NRIC + '.csv'
    
        for x in os.listdir('Notification'):
            if x == file:
                path = 'Notification/' + x
                with open(path, 'r', encoding='UTF8') as f:
                    reader = csv.reader(f)
                    for notification in reader:
                        NOTIFICATIONS.append(notification)
                return True
        return False
    
    def check_notifications(self, bool):
        if bool and len(NOTIFICATIONS) != 0:
            print("\n+++++++++++++++++++++ NOTIFICATIONS +++++++++++++++++++++")
            for x in NOTIFICATIONS:
                print (x)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            print("\n+++++++++++++++++++++ NO NOTIFICATION +++++++++++++++++++++")

    def validate_nric(self, nric):
        if (len(nric) == 9 and nric[1:-1].isdigit() and nric[0].isalpha() and nric[-1].isalpha()):
            return True
        else:
            return False

    def generate_nric_request(self, request, nric):
        for i, char in enumerate(request):
            if i >= len(nric):
                temp_nric = "" 
            else:
                temp_nric = nric[i]
            yield safeentry_pb2.get_notification(message=char, nric = temp_nric)

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
                    date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                    response = self.safe_entry_stub.CheckIn(safeentry_pb2.CheckRequest(nric = NRIC, location = LOCATIONS[int(location_input)-1], datetime = date_time))

                    if response.status:
                        print('Successfully checked in at ' + LOCATIONS[int(location_input)-1] + ' during ' + date_time)
                        self.user_ui()
                    else:
                        print('Error! Please Check In Again!\n')
                        self.check_in()
                else:
                    print('\nInvalid Input! Please Try Again!\n')
                    continue

            elif user_input == '2':
                print("List Of Locations: ")
                self.print_locations()

                nric_list = []
                location_input = input("\nPlease Select Location: ")
                
                if location_input.isdigit() or int(location_input) <= LOCATIONS.count:

                    number_input = input("\nNumber Of People: ")

                    if number_input.isdigit():
                        nric_list.append(NRIC)
                        for x in number_input:
                            nric_input = input("\nNRIC for Person " + x + ": ")
                            nric_list.append(nric_input.upper())
                            
                        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                        response = self.safe_entry_stub.CheckIn(safeentry_pb2.CheckRequest(nric = nric_list, location = LOCATIONS[int(location_input)-1], datetime = date_time))

                        if response.status:
                            print('Successfully checked in at ' + LOCATIONS[int(location_input)-1] + ' during ' + date_time)
                            self.user_ui()
                        else:
                            print('Error! Please Check In Again!\n')
                            self.check_in()
                    else:
                        print('\nInvalid Input! Please Try Again!\n')
                        continue
                else:
                    print('\nInvalid Input! Please Try Again!\n')
                    continue
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
                date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                response = self.safe_entry_stub.CheckOut(safeentry_pb2.CheckRequest(nric = NRIC, location = LOCATIONS[int(location_input)-1], datetime = date_time))

                if response.status:
                    print('Successfully checked out at ' + LOCATIONS[int(location_input)-1] + ' during ' + date_time)
                    self.user_ui()
                else:
                    print('Error! Please Check Out Again!\n')
                    self.check_out()
            else:
                print('\nInvalid Input! Please Try Again!\n')
                continue

    def change_password(self):
        while(1):
            print('\n++++++++ CHANGE PASSWORD ++++++++\n')
            old_password = input("Please Input Current Password: ")
            new_password = input("\nPlease Input New Password: ")
            confirm = input("\nConfirm? (y/n): ")

            if confirm.lower() == 'y':
                response = self.password_stub.ChangePassword(safeentry_pb2.get_password(nric = NRIC, old_password = old_password, new_password = new_password))
                if response.response == 'success':
                    print('You have successfully changed your password!')
                    self.user_ui()
                elif response.response == 'error1':
                    print('New password must be different from your current password!')
                else:
                    print('Wrong password!')
            elif confirm.lower() == 'n':
                self.change_password()
            else:
                print('Invalid Input!')
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
        for i in response_history.response:
            print(i)
        exit()

    def declare_location(self):
        while(1):
            print("List Of Locations: ")
            self.print_locations()

            location_input = input("\nPlease Select Location: ")
            if location_input.strip().isdigit() or int(location_input) <= LOCATIONS.count:
                nric = input('Enter NRIC: ')
                date_entry = input('Enter checked in datetime in YYYY-MM-DD HH:MM format (e.g., 2022-06-20 10:30): ')
                is_date = self.check_date_format(date_entry)
                if is_date:      
                    d = datetime.strptime(date_entry, "%Y-%m-%d %H:%M")
                    d = d.strftime('%Y-%m-%dT%H:%M:%S.%f')
                    
                    response_location = self.location_stub.DeclareLocation(safeentry_pb2.get_location_data(location = LOCATIONS[int(location_input)-1], nric = nric, datetime = d))        
                    if response_location.response == 'success':
                        n = safeentry_pb2.DeclarationInfo()  # create protobug message (called DeclarationInfo)
                        n.message = str(response_location.noti_list)  # set the actual message of the declaration
                        self.notification_stub.ReceiveDeclaration(n)  # send the DeclarationInfo to the server
                        self.officer_ui()

                    else:
                        print("\nNRIC not found in system!")
                    
            
                else:
                    print('\nInvalid Input! Please Try Again!\n')
                    continue
            else:
                print('\nInvalid Input! Please Try Again!\n')
                continue

    def check_date_format(self, date):
        regex = re.compile("[0-9]{4}\-[0-9]{2}\-[0-9]{2}\ [0-9]{2}\:[0-9]{2}")
        match = re.match(regex, date)

        if (match):
            return True
        else: 
            return False     

if __name__ == '__main__':
    logging.basicConfig()
    client = SafeEntry()
    client.run()