class Room:
    def __init__(self,arg1,arg2):
        self.roomName = arg1 + " " + arg2
        self.timeSlotsCount = 28
        self.timeSlots = [0] * self.timeSlotsCount
        self.roomCapacity = 0       #switch to arg3 at some point
    def addClassTime(self,timeSlot):
        self.timeSlots[timeSlot]=1      #switch data to new argument, of type "roomEvent"
    def removeClassTime(self,timeSlot):
        self.timeSlots[timeSlot]=0
    def getRoomName(self):
        return self.roomName