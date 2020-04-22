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
event1 = Events("CMSC","100"," ","01","Professor X","MW1",200)


room5.addEvent(1,event1)
event2 = Events("BIO","110"," ","02"," ","TTH2",50)
print(event2.getSubject()+" "+event2.getCourseNum())
event2.getSubject()
print("DEBUG")
print("DEBUG")
print(room5.getEvent(1).getSubject()+" "+event2.getCourseNum())

roomList = [room1,room2,room3,room4,room5]

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
window1 = GUI_Main(interface,roomList)

testBuilding = input("Building Name: ")
testRNumber = input("Room Number: ")
testCapacity = input("Room Capacity: ")
room6 = Room(testBuilding,testRNumber,testCapacity)
roomList.append(room6)
window1.buildItems(roomList,0,0)

interface.mainloop()
