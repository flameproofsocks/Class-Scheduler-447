###
# Created on Apr 6,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###
from Room import Room
from GUI_Main import GUI_Main
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

import psycopg2
import psycopg2.extensions
import os

connection = psycopg2.connect(user = "postgres",
                                  password = "bippy",
                                  host = "localhost",
                                  port = "5432",
                                  database = "447ver1")
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

# room1 = Room("BIO","101")
# room2 = Room("BIO","102")
# room3 = Room("MATH","101")
# room4 = Room("MATH","201")
# room5 = Room("ENG","101")
# room5.addEvent(1)

# roomList = [room1,room2,room3,room4,room5]

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Class Name: ")
testRNumber = input("Room Number: ")
room6 = Room(testBuilding,testRNumber)
roomList.append(room6)
window1.buildItems(roomList)

interface.mainloop()
