from tkinter import filedialog

def selectFile(self,fileName):
        fileName = filedialog.askopenfilename()

def addFile(self,fileName,fileType):
        f = open(fileName,'r')
        fType = fileType;       #0 for room list, 1 for event list,see examples provided for format

        #parse data into proper fields, send to database