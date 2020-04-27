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
        self.timeSlotsCount = 28    #8:00AM-9:30PM in 30 min increments,see comment at bottom for complete breakdown
        self.timeSlots = [placeholdEvent] * self.timeSlotsCount  
        self.roomCapacity = arg3       
        self.dayOfWeek = 1  #int value for day of week, see comment at bottom for complete breakdown
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

###
#timeSlotCount details:
#0 - 8:00 AM
#1 - 8:30 AM
#2 - 9:00 AM
#3 - 9:30 AM
#4 - 10:00 AM
#5 - 10:30 AM
#6 - 11:00 AM
#7 - 11:30 AM
#8 - 12:00 PM
#9 - 12:30 PM
#10 - 1:00 PM
#11 - 1:30 PM
#12 - 2:00 PM
#13 - 2:30 PM
#14 - 3:00 PM
#15 - 3:30 PM
#16 - 4:00 PM
#17 - 4:30 PM
#18 - 5:00 PM
#19 - 5:30 PM
#20 - 6:00 PM
#21 - 6:30 PM
#22 - 7:00 PM
#23 - 7:30 PM
#24 - 8:00 PM
#25 - 8:30 PM
#26 - 9:00 PM
#27 - 9:30 PM
#
#daysofWeek details:
#1 - Monday
#2 - Tuesday
#3 - Wednesday
#4 - Thursday
#5 - Friday
###

