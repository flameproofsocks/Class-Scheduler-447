class Room:
    def __init__(self,arg1,arg2):
        self.roomName = arg1 + " " + arg2
        self.timeSlotsCount = 5
        self.timeSlots = [0] * self.timeSlotsCount
    def addClassTime(self,timeSlot):
        self.timeSlots[timeSlot]=1
    def removeClassTime(self,timeSlot):
        self.timeSlots[timeSlot]=0
    def getRoomName(self):
        return self.roomName