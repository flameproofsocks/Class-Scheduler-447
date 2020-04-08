###
# Created on Apr 8,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###

from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

class GUI_Main:
    def __init__(self,master,roomList):
        master.title("Schedule Planner v0.01")

        self.canvas_master = Canvas(master)
        self.main_font = Font(family = "Arial",size = 15)

        self.canvas_master.pack(side="left",fill="both",expand=True)

        self.canvas_rooms = Canvas(self.canvas_master,height=25)
        self.frame_rooms = Frame(self.canvas_rooms)

        self.canvas_times = Canvas(self.canvas_master,width = 55)
        self.frame_times = Frame(self.canvas_times)

        self.canvas_classes = Canvas(self.canvas_master)
        self.frame_classes = Canvas(self.canvas_classes)

        self.sbY = Scrollbar(self.canvas_master,command=self.adjustYview)
        self.sbX = Scrollbar(self.canvas_master,orient='horizontal',command = self.adjustXview)

        self.canvas_rooms.grid(row=0,column=1)
        self.canvas_times.grid(row=1,column=0)
        self.canvas_classes.grid(row=1,column=1)

        self.canvas_rooms.create_window((0,0),window=self.frame_rooms,anchor = "nw")
        self.canvas_times.create_window((0,0),window=self.frame_times,anchor='nw')
        self.canvas_classes.create_window((0,0),window=self.frame_classes,anchor='nw')

        self.sbY.grid(row = 1, column = 2, sticky = "ns")
        self.sbX.grid(row=2,column=1,stick="ew")

        self.frame_classes.bind("<Configure>",self.function1)
        self.frame_times.bind("<Configure>",self.function1)
        self.frame_rooms.bind("<Configure>",self.function1)

        self.buildItems(roomList)
        
    def buildItems(self,roomList):
        w = len(roomList * 111)
        self.canvas_rooms.configure(width = w)
        self.canvas_classes.configure(width = w)

        self.gridWidth = 10
        self.gridHeight = 1
        
        i = 1
        flag = 0
        timeDisplay = 8.0 #start at 8 AM
        for item in roomList:
            self.label_room = Label(self.frame_rooms,text = item.getRoomName(), font = self.main_font,width = self.gridWidth,height = self.gridHeight,bd = 2,relief= "groove")
            self.label_room.grid(row=0 ,column = i, sticky = W)
            i = i + 1
            #time slots on left side
            for x in range(len(item.timeSlots)):
                if(flag==0):
                    if(timeDisplay < 1):
                        timeDisplay = timeDisplay + 12
                    timeDisplayString = str(format(timeDisplay,".2f"))
                    timeDisplayString = timeDisplayString.replace(".",":")
                    self.label_time = Label(self.frame_times, text = timeDisplayString, font = self.main_font,height = self.gridHeight)
                    self.label_time.grid(row = x + 1,column = 0, sticky = W)
                    timeDisplay = (timeDisplay + .3)
                    if(round(timeDisplay) > timeDisplay):
                        timeDisplay = round(timeDisplay)
                        timeDisplay = (timeDisplay) % 12
            flag = 1
            #events in each room per time slot
            for time in range(len(item.timeSlots)):
                self.label_class = Label(self.frame_classes, text = item.timeSlots[time], font = self.main_font,width = self.gridWidth,height = self.gridHeight,bg="red")
                self.label_class.grid(row = time + 1, column = i, sticky = W)

    def function1(self,event):
        self.canvas_classes.configure(scrollregion=self.canvas_classes.bbox("all"))
        self.canvas_times.configure(scrollregion=self.canvas_times.bbox("all"))
        self.canvas_rooms.configure(scrollregion=self.canvas_rooms.bbox("all"))

    def adjustYview(self,*args):
        self.canvas_classes.yview(*args)
        self.canvas_times.yview(*args)

    def adjustXview(self,*args):
        self.canvas_classes.xview(*args)
        self.canvas_rooms.xview(*args)