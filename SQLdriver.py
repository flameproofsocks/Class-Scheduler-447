###
# Created on Apr 6,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###
from Room import Room
from GUI_Search import GUI_Main
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

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Class Name: ")

query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
cursor.execute(query1)

roomList = []
for building, roomnum in cursor.fetchall():
    roomList.append(Room(building, str(roomnum) ) )

# testRNumber = input("Room Number: ")
# room6 = Room(testBuilding,testRNumber)
# roomList.append(room6)
window1.buildItems(roomList)

interface.mainloop()
