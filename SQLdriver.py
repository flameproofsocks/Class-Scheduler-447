###
# Created on Apr 6,2020
# Updated April 22 2020
#
# @author: Brady Ronayne
# SHould take from online database
###
from Room import Room
from Events import Events
from GUI_Main import GUI_Main
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import DBqueries

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

###reload events
# cursor.execute(DBqueries.queryClearAll)
# cursor.execute(DBqueries.queryLoadRooms)
# cursor.execute("INSERT INTO prof VALUES(1, 'John', 'Smith', 'Chalk Allergy', 'www.website.com', 'A generic teacher, hates chalk, talks loudly, students still fall asleep' ) ON CONFLICT DO NOTHING;")
# cursor.execute(DBqueries.queryLoadEvents)

query1 = "select roomid, building, roomnum, capacity from rooms"
cursor.execute(query1)

roomList = []
idList = []
for roomid, building, roomnum, capacity in cursor.fetchall():
    roomList.append(Room(building, str(roomnum) , str(capacity)) )
    idList.append(roomid)


# self.subject = arg1
# self.courseNum = arg2
# self.version = arg3
# self.section = arg4
# self.instructor = arg5
# self.time = arg6
# self.capacity = arg7
#event1 = Events("CMSC","100"," ","01","Professor X","MW1",200)

#Code to add events within the room
j = 1
cursor2 = connection.cursor()
for i in range(len(roomList)):
    query1 = "Select resID, eventName, courseNum, profID from events where roomID = " + str(idList[i]) 
    cursor2.execute(query1)
    for resID, eventName, courseNum, profID in cursor2.fetchall():
        roomList[i].addEvent(j,Events(eventName, courseNum," ","02",profID,"TTH1",50))
        j += 1 #index for adding events
    


interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Class Name: ")

if(window1.entry_addRoom_name.get() != ""):

    #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
    cursor.execute(DBqueries.findIndexRooms)
    nextID = int(cursor.fetchone() ) + 1 #next index
    query1 = "INSERT INTO rooms VALUES("+str(nextID)+", '"+ str(window1.entry_addRoom_name.get()) + "', '" + str(window1.entry_addRoom_number.get()) + "', 30, 'Classroom') ON CONFLICT DO NOTHING;"
    cursor.execute(query1)

if(window1.entry_addEvent_subject.get() != ""):

    #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
    cursor.execute(DBqueries.findIndexEvents)
    nextID = int(cursor.fetchone()[0] ) + 1 #next index
    query1 = "INSERT INTO events VALUES("+str(nextID)+", '"+ str(window1.entry_addEvent_subject.get()) + "', '" + str(window1.entry_addEvent_courseNum.get()) + "', 10101, '10:00:00', '11:15:00', 'Class from UI', " + str(window1.entry_addEvent_instructor.get()) +", 1) ON CONFLICT DO NOTHING;"
    cursor.execute(query1)

# if(window1.entry_search_building.get() != ""):
#     query1 = "Select building, roomnum from rooms where building = '" + str(window1.entry_search_building.get())+"' and roomnum = '"+ str(window1.entry_search_num.get()) + "';"
#     cursor.execute(query1)
# else:
#     query1 = "select building, roomnum, capacity from rooms"
#     cursor.execute(query1)

# roomList = []
# for building, roomnum, capacity in cursor.fetchall():
#     roomList.append(Room(building, str(roomnum) , str(capacity)) )

# # testRNumber = input("Room Number: ")
# # room6 = Room(testBuilding,testRNumber)
# # roomList.append(room6)
# window1.buildItems(roomList)

# interface.mainloop()