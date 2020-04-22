###
# Created on Apr 8,2020
#
# @author: Brett Hornick
# bhornic1@umbc.edu
###
from Events import Events
class Room:
    def __init__(self,arg1,arg2,arg3):
        placeholdEvent = Events()
        self.buildingName = arg1    
        self.roomNumber = arg2
        self.roomName = arg1 + " " + arg2   #Combination of room name and number, for ease of printing data
        self.timeSlotsCount = 28    #8:00AM-9:30PM in 30 min increments
        self.timeSlots = [placeholdEvent] * self.timeSlotsCount  
        self.roomCapacity = 0       #switch to arg3 at some point
    def getBuidlingName(self):
        return self.buildingName
    def getRoomNumber(self):
        return self.roomNumber
    def getRoomName(self):
        return self.roomName
    def getRoomCapacity(self):
        return self.roomCapacity
    def addEvent(self,timeSlot,newEvent):
        self.timeSlots[timeSlot]=newEvent     #switch data to new argument, of type "roomEvent"
    def removeEvent(self,timeSlot):
        self.timeSlots[timeSlot]=0
    def getEvent(self,timeSlot):
        return self.timeSlots[timeSlot]