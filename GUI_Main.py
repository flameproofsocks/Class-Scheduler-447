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
#import guiOperations as gOp
import guiOpTest as gOp
from Room import Room
from Events import Events

class GUI_Main:
    def __init__(self,master,roomList):
        master.title("Schedule Planner v0.1")
        self.placeholderEvent = Events()

#Options Section
        self.frame_OptionMaster = Frame(master,height = 100)
        self.frame_OptionMaster.pack(side="top",fill="both",expand=True)

#Open file options
        self.frame_openFiles = Frame(self.frame_OptionMaster,width=200)
        self.buildOpenFilesFrame(self.frame_openFiles)

#Add room outside of file
        self.frame_addRoom = Frame(self.frame_OptionMaster)
        self.buildAddRoomFrame(self.frame_addRoom)

#Add Event(class) options outside of file
        self.frame_addEvent = Frame(self.frame_OptionMaster)
        self.buildAddEventFrame(self.frame_addEvent)

#Search options
        self.frame_search = Frame(self.frame_OptionMaster)
        self.buildSearchFrame(self.frame_search)

#Grid option frames
        self.frame_openFiles.grid(column=1,row=0)
        self.frame_addRoom.grid(column=2,row=0)
        self.frame_addEvent.grid(column=3,row=0)
        self.frame_search.grid(column=4,row=0)

#Event information Section
        self.frame_EventInfo = Frame(master,height = 100)
        self.frame_EventInfo.pack(side="bottom",fill="both",expand=True)
        self.buildEventInfoFrame(self.frame_EventInfo,self.placeholderEvent)
        
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

        self.buildItems(roomList,0,0)
  
    def buildItems(self,roomList,startTime,endTime):
        #Cleans frame, incase there are items in it:
        for widget in self.frame_classes.winfo_children():
            widget.destroy()
        for widget in self.frame_times.winfo_children():
            widget.destroy()
        for widget in self.frame_rooms.winfo_children():
            widget.destroy()

        sTime = 0 + startTime #starts at 0, max eTime
        eTime = 28 - endTime  #starts at max of roomList timeslots, should be 28, min sTime
        #NO ERROR CHECKING, please do error checing before calling buildItems
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
            print("item %d",i)
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
                self.placeholderEvent = item.getEvent(time)
                self.button_event = Button(self.frame_classes, text = self.placeholderEvent.getSubject()+" "+self.placeholderEvent.getCourseNum() , font = self.font_DisplayItems,width = self.gridWidth,height = self.gridHeight)
                self.button_event.configure(command = lambda: self.buildEventInfoFrame(self.frame_EventInfo, self.placeholderEvent))
                self.button_event.grid(row = time + 1, column = i, sticky = W)

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
    
    def buildOpenFilesFrame(self,master):
        # self.fb1Var = 0
        # self.fb2Var = 0
        self.fileName = " "
        self.fileType = 0 #0 for room list, 1 for class list
        self.button_selectFile = Button(master,text="Select File",command=lambda: fOp.selectFile(self,self.fileName))
        self.label_fileType = Label(master,text="Select File Type:")
        self.rbutton_fileType1 = Radiobutton(master,text="Room List",variable=self.fileType, value = 0)
        self.rbutton_fileType2 = Radiobutton(master,text="Class List",variable=self.fileType, value = 1)
        self.button_addFile = Button(master,text="Add Selected File",command=lambda:  fOp.addFile(self,self.fileName,self.fileType ) )
        #fOp.addFile(self,self.fileName,self.fileType
        self.button_selectFile.grid(row=1)
        self.label_fileType.grid(row=2)
        self.rbutton_fileType1.grid(row=3)
        self.rbutton_fileType2.grid(row=4)
        self.button_addFile.grid(row=5)

    def buildAddRoomFrame(self,master):
        self.label_addRoom_title = Label(master,text="Add Room")
        self.label_addRoom_name = Label(master,text="Room Name: ")
        self.entry_addRoom_name = Entry(master)
        self.label_addRoom_number = Label(master,text="Room Number:")
        self.entry_addRoom_number = Entry(master)
        self.label_addRoom_capacity = Label(master,text="Capacity: ")
        self.entry_addRoom_capacity = Entry(master)
        self.button_addRoom = Button(master,text="Add") #command to be added when file reading is complete

        self.label_addRoom_title.grid(row=1,columnspan=2)
        self.label_addRoom_name.grid(row=2,column=1)
        self.entry_addRoom_name.grid(row=2,column=2)
        self.label_addRoom_number.grid(row=3,column=1)
        self.entry_addRoom_number.grid(row=3,column=2)
        self.label_addRoom_capacity.grid(row=4,column=1)
        self.entry_addRoom_capacity.grid(row=4,column=2)
        self.button_addRoom.grid(row=5,columnspan=2)

    def buildAddEventFrame(self,master):
        self.label_addEvent_title = Label(master,text="Add Class")
        self.label_addEvent_subject = Label(master,text="Subject: ")
        self.entry_addEvent_subject = Entry(master)
        self.label_addEvent_courseNum = Label(master,text="Course Number: ")
        self.entry_addEvent_courseNum = Entry(master)
        self.label_addEvent_section = Label(master,text="Section Number: ")
        self.entry_addEvent_section = Entry(master)
        self.label_addEvent_instructor = Label(master,text="Instructor: ")
        self.entry_addEvent_instructor = Entry(master)
        self.label_addEvent_time = Label(master,text="Prefered time: ")
        self.entry_addEvent_time = Entry(master)
        self.label_addEvent_capacity = Label(master,text="Capacity: ")
        self.entry_addEvent_capacity = Entry(master)
        self.button_addEvent = Button(master,text="Add") #command to be added when file reading is complete

        self.label_addEvent_title.grid(row=0)
        self.label_addEvent_subject.grid(row=1,column=0)
        self.entry_addEvent_subject.grid(row=1,column=1)
        self.label_addEvent_courseNum.grid(row=2,column=0)
        self.entry_addEvent_courseNum.grid(row=2,column=1)
        self.label_addEvent_section.grid(row=3,column=0)
        self.entry_addEvent_section.grid(row=3,column=1)
        self.label_addEvent_instructor.grid(row=4,column=0)
        self.entry_addEvent_instructor.grid(row=4,column=1)
        self.label_addEvent_time.grid(row=5,column=0)
        self.entry_addEvent_time.grid(row=5,column=1)
        self.label_addEvent_capacity.grid(row=6,column=0)
        self.entry_addEvent_capacity.grid(row=6,column=1)
        self.button_addEvent.grid(row=7,column=1,columnspan=2)

    def buildSearchFrame(self,master):
        self.cb1Var = IntVar()
        self.cb1Var.set(1)
        self.cb2Var = IntVar()
        self.label_search_title = Label(master,text="Search")
        self.label_search_keyword = Label(master,text="Keywords: ")
        self.entry_search_keyword = Entry(master)
        self.label_search_type = Label(master,text="Search catagories: ")
        self.checkbox_search_room = Checkbutton(master,text="Rooms",variable=self.cb1Var, onvalue = 1, offvalue = 0)
        self.checkbox_search_classes = Checkbutton(master,text="Classes",variable = self.cb2Var, onvalue = 1, offvalue = 0)
        self.button_search = Button(master,text="Search",command = lambda: self.searchDB(self.entry_search_keyword,self.cb1Var,self.cb2Var,0,0) ) #add command at later date

        self.label_search_title.grid(row=0)
        self.label_search_keyword.grid(row=1,column=0)
        self.entry_search_keyword.grid(row=1,column=1)
        self.label_search_type.grid(row=2,column=0)
        self.checkbox_search_room.grid(row=3,column=1)
        self.checkbox_search_classes.grid(row=4,column=1)
        self.button_search.grid(row=5,column=1)

    def searchDB(self,keywords,searchRooms,searchEvents,sTime,eTime):
        print("Testing Search: ", str(keywords.get()))
        roomList = gOp.searchDB(self,keywords,searchRooms,searchEvents)
        self.buildItems(roomList,sTime,eTime)

    def buildEventInfoFrame(self,master,displayEvent):
        for widget in master.winfo_children():
            widget.destroy()

        self.label_eventInfo_courseName = Label(master,text="Course Name: " +displayEvent.getSubject() + " "+ displayEvent.getCourseNum())
        self.label_eventInfo_section = Label(master,text="Section: "+displayEvent.getSection())
        self.label_eventInfo_instructor = Label(master,text="Instructor: "+displayEvent.getInstructor())
        self.label_eventInfo_capacity= Label(master,text="Class Capacity"+str(displayEvent.getCapacity()))

        self.label_eventInfo_courseName.grid(row=0,column=0)
        self.label_eventInfo_section.grid(row=1,column=0)
        self.label_eventInfo_instructor.grid(row=2,column=0)
        self.label_eventInfo_capacity.grid(row=3,column=0)