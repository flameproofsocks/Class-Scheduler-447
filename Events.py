###
# Created on Apr 13,2020
# @author: Jordon Malcolm
# jordonm1@umbc.edu
###
class Events:
    def __init__(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.subject = arg1
        self.courseNum = arg2
        self.version = arg3
        self.section = arg4
        self.instructor = arg5
        self.time = arg6
        self.capacity = arg7
    def getSubject(self):
        return self.subject
    def getCourseNum(self):
        return self.courseNum
    def getVersion(self):
        return self.version
    def getSection(self):
        return self.section
    def getInstructor(self):
        return self.instructor
    def getTime(self):
        return self.time
    def getCapacity(self):
        return self.capacity