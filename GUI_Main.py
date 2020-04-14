###
# Created on Apr ,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###

from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import fileOperations as fOp

class GUI_Main:
    def __init__(self,master,roomList):
        master.title("Schedule Planner v0.1")

#Options Section
        self.frame_OptionMaster = Frame(master,height = 100)
        self.frame_OptionMaster.pack(side="top",fill="both",expand=True)

#Open file options
        self.fileName = " "
        self.fileType = 0 #0 for room list, 1 for class list
        self.frame_openFiles = Frame(self.frame_OptionMaster,width=200)
        self.button_selectFile = Button(self.frame_openFiles,text="Select File",command=lambda: fOp.selectFile(self,self.fileName))
        self.label_fileType = Label(self.frame_openFiles,text="Select File Type:")
        self.rbutton_fileType1 = Radiobutton(self.frame_openFiles,text="Room List",variable=self.fileType,value=0)
        self.rbutton_fileType2 = Radiobutton(self.frame_openFiles,text="Class List",variable=self.fileType,value=1)
        self.button_addFile = Button(self.frame_openFiles,text="Add Selected File",command=lambda: fOp.addFile(self,self.fileName,self.fileType))

        self.button_selectFile.grid(row=1)
        self.label_fileType.grid(row=2)
        self.rbutton_fileType1.grid(row=3)
        self.rbutton_fileType2.grid(row=4)
        self.button_addFile.grid(row=5)

#Add room options outside of file
        self.frame_addRoom = Frame(self.frame_OptionMaster,width=50,bg="yellow")
        self.label_addRoom_title = Label(self.frame_addRoom,text="Add Room")
        self.label_addRoom_name = Label(self.frame_addRoom,text="Room Name: ")
        self.entry_addRoom_name = Entry(self.frame_addRoom)
        self.label_addRoom_number = Label(self.frame_addRoom,text="Room Number:")
        self.entry_addRoom_number = Entry(self.frame_addRoom)
        self.label_addRoom_capacity = Label(self.frame_addRoom,text="Capacity: ")
        self.entry_addRoom_capacity = Entry(self.frame_addRoom)

        self.label_addRoom_title.grid(row=1,columnspan=2)
        self.label_addRoom_name.grid(row=2,column=1)
        self.entry_addRoom_name.grid(row=2,column=2)
        self.label_addRoom_number.grid(row=3,column=1)
        self.entry_addRoom_number.grid(row=3,column=2)
        self.label_addRoom_capacity.grid(row=4,column=1)
        self.entry_addRoom_capacity.grid(row=4,column=2)



#Add Event(class) options outside of file
        self.frame_addEvent = Frame(self.frame_OptionMaster,width=50,bg="red")


        self.frame_openFiles.grid(column=1)
        self.frame_addRoom.grid(column=2)
        self.frame_addEvent.grid(column=3)
        
#Data Display Section
        self.canvas_DataMaster = Canvas(master)

        self.canvas_DataMaster.pack(side="bottom",fill="both",expand=True)

        self.canvas_rooms = Canvas(self.canvas_DataMaster,height=25)
        self.frame_rooms = Frame(self.canvas_rooms)

        self.canvas_times = Canvas(self.canvas_DataMaster,width = 55)
        self.frame_times = Frame(self.canvas_times)

        self.canvas_classes = Canvas(self.canvas_DataMaster)
        self.frame_classes = Canvas(self.canvas_classes)

        self.sbY = Scrollbar(self.canvas_DataMaster,command=self.adjustYview)
        self.sbX = Scrollbar(self.canvas_DataMaster,orient='horizontal',command = self.adjustXview)

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
        self.font_DisplayItems = Font(family = "Arial",size = 15)

        self.gridWidth = 10
        self.gridHeight = 1
        
        i = 1
        flag = 0
        timeDisplay = 8.0 #start at 8 AM
        for item in roomList:
            self.label_room = Label(self.frame_rooms,text = item.getRoomName(), font = self.font_DisplayItems,width = self.gridWidth,height = self.gridHeight,bd = 2,relief= "groove")
            self.label_room.grid(row=0 ,column = i, sticky = W)
            i = i + 1
            #time slots on left side
            for x in range(len(item.timeSlots)):
                if(flag==0):
                    if(timeDisplay < 1):
                        timeDisplay = timeDisplay + 12
                    timeDisplayString = str(format(timeDisplay,".2f"))
                    timeDisplayString = timeDisplayString.replace(".",":")
                    self.label_time = Label(self.frame_times, text = timeDisplayString, font = self.font_DisplayItems,height = self.gridHeight)
                    self.label_time.grid(row = x + 1,column = 0, sticky = W)
                    timeDisplay = (timeDisplay + .3)
                    if(round(timeDisplay) > timeDisplay):
                        timeDisplay = round(timeDisplay)
                        timeDisplay = (timeDisplay) % 12
            flag = 1
            #events in each room per time slot
            for time in range(len(item.timeSlots)):
                self.label_class = Label(self.frame_classes, text = item.timeSlots[time], font = self.font_DisplayItems,width = self.gridWidth,height = self.gridHeight)
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