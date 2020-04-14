from tkinter import filedialog

def selectFile(self,fileName):
        fileName = filedialog.askopenfilename()

def addFile(self,fileName,fileType):
        f = open(fileName,'r')
        fType = fileType;
        #pass data to 