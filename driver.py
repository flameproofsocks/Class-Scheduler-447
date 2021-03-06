###
# Created on Apr 6,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###
from Room import Room
from Events import Events
from GUI_Main import GUI_Main
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk


room1 = Room("BIO","101",200)
room2 = Room("BIO","102",100)
room3 = Room("MATH","101",50)
room4 = Room("MATH","201",25)
room5 = Room("ENG","101",25)
room6 = Room("CMSC", "103", 30)
room7 = Room("CMSC", "202", 40)
event1 = Events("CMSC","100"," ","01","Professor X","MW1",200)


room5.addEvent(1,event1)
event2 = Events("CMSC","447"," ","01","Kartchner","MW10",30)
room5.addEvent(27,event2)
roomList = [room1,room2,room3,room4,room5, room6, room7]

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testNameOfUser = input("Your Name: ")
testBuilding = input("Building Name: ")
testRNumber = input("Room Number: ")
testCapacity = input("Room Capacity: ")
testTimeNeeded = input("Time Required in Minutes: ")
room6 = Room(testBuilding,testRNumber,testCapacity)
roomList.append(room6)
window1.buildItems(roomList,0,0)
window1.buildEventInfoFrame(window1.frame_EventInfo,event1)

interface.mainloop()
