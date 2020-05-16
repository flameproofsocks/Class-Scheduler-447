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


print("DEBUGGING: ")
cursor.execute("select * from Events")
print(cursor.fetchall())

#EVENTS
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
    query1 = "Select resID, eventName, courseNum, profID, startTime from events where roomID = " + str(idList[i]) + " Limit 14"
    cursor2.execute(query1)
    j = 1
    for resID, eventName, courseNum, profID, startTime in cursor2.fetchall():
        timeSlot = (int(str(startTime)[:2]) - 8)*2 // 1
        roomList[i].addEvent(timeSlot,Events(str(startTime)[:4] +"-" + str(timeSlot), courseNum," ","02",profID,"TTH" + str(timeSlot) ,50))
        j += 1 #index for adding events
    

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Class Name: ")
