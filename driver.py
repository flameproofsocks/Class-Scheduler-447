###
# Created on Nov 19, 2018
#
# @author: Brett
###
from TestClasses import Room
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

class GUI_Main:
    def __init__(self, master, roomList):
        self.master = master
        
        master.title("Schedule Planner v0.00001")
        self.frame_roomList = Frame(master)
        self.main_font = Font(family = "Arial",size = 15)

        self.frame_roomList.grid()
        i = 1
        flag = 0
        timeDisplay = 8.0 #start at 8 AM
        for item in roomList:
            self.label_room = Label(self.frame_roomList,text = item.getRoomName(), font = self.main_font)
            self.label_room.grid(row=0 ,column = i, sticky = W)
            i = i + 1
            #time slots on left side
            for x in range(len(item.timeSlots)):
                if(flag==0):
                    if(timeDisplay < 1):
                        timeDisplay = timeDisplay + 12
                    timeDisplayString = str(format(timeDisplay,".2f"))
                    timeDisplayString = timeDisplayString.replace(".",":")
                    self.label_time = Label(self.frame_roomList, text = timeDisplayString, font = self.main_font)
                    self.label_time.grid(row = x + 1,column = 0, sticky = W)
                    timeDisplay = (timeDisplay + .3)
                    if(round(timeDisplay) > timeDisplay):
                        timeDisplay = round(timeDisplay)
                        timeDisplay = (timeDisplay) % 12
            flag = 1
            #events in each room per time slot
            for time in range(len(item.timeSlots)):
                self.label_class = Label(self.frame_roomList, text = item.timeSlots[time], font = self.main_font)
                self.label_class.grid(row = time + 1, column = i, sticky = W)

room1 = Room("BIO","101")
room2 = Room("BIO","102")
room3 = Room("MATH","101")
room4 = Room("MATH","201")
room5 = Room("ENG","101")
room5.addClassTime(1)

roomList = [room1,room2,room3,room4,room5]

interface = Tk()
interface.geometry("800x600")
interface.configure(bg="black")
my_gui = GUI_Main(interface,roomList)
interface.mainloop()