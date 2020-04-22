###
# Created on Apr 6,2020
# Updated April 22 2020
#
# @author: Brady Ronayne
# SHould take from online database
###
from Room import Room
from GUI_Search import GUI_Main
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

import psycopg2
import psycopg2.extensions
import os

# connection = psycopg2.connect(user = "postgres",
#                                   password = "bippy",
#                                   host = "localhost",
#                                   port = "5432",
#                                   database = "447ver1")

connection = psycopg2.connect(user = "postgres",
                                  password = "software447",
                                  host = "database447.cst3jimtz2ge.us-east-2.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ClassScheduler")

                                  
#setup database
connection.autocommit = True
cursor = connection.cursor()

# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

query1 = "select building, roomnum from rooms"
cursor.execute(query1)

roomList = []
for building, roomnum in cursor.fetchall():
    roomList.append(Room(building, str(roomnum) ) )

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Class Name: ")

if(window1.entry_addRoom_name.get() != ""):

    #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
    query1 = "INSERT INTO rooms VALUES(7, '"+ str(window1.entry_addRoom_name.get()) + "', '" + str(window1.entry_addRoom_number.get()) + "', 30, 'Classroom') ON CONFLICT DO NOTHING;"
    cursor.execute(query1)

if(window1.entry_search_building.get() != ""):
    query1 = "Select building, roomnum from rooms where building = '" + str(window1.entry_search_building.get())+"' and roomnum = '"+ str(window1.entry_search_num.get()) + "';"
    cursor.execute(query1)
else:
    query1 = "select building, roomnum from rooms"
    cursor.execute(query1)

roomList = []
for building, roomnum in cursor.fetchall():
    roomList.append(Room(building, str(roomnum) ) )

# testRNumber = input("Room Number: ")
# room6 = Room(testBuilding,testRNumber)
# roomList.append(room6)
window1.buildItems(roomList)

interface.mainloop()