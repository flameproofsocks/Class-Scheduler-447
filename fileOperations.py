# from tkinter import filedialog

# def selectFile(self,fileName):
#         fileName = filedialog.askopenfilename()

# def addFile(self,fileName,fileType):
#         f = open(fileName,'r')
#         fType = fileType;       #0 for room list, 1 for event list,see examples provided for format

#         #parse data into proper fields, send to database

from tkinter import filedialog
import DBqueries

import psycopg2
import psycopg2.extensions
import os

from Room import Room
from Events import Events

connection = psycopg2.connect(user = "postgres",
                                  password = "software447",
                                  host = "database447.cst3jimtz2ge.us-east-2.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ClassScheduler")

                                  
#setup database
connection.autocommit = True
cursor = connection.cursor()



DEPART = 0
COURSE_NUM = 1
COURSE_NAME = 2
SEC_NAME = 3
SECTION = 4
INSTRUCTORF = 5
TIME = 6
CAP = 7
INSTRUCTORL = 6
TIME2 = 7
CAP2 = 8

ROOM = 0
CAPACITY = 1

MWF = "10101"
MW = "10100"
TT = "01010"


def insertRoomBuild(arr):
    command = "INSERT INTO rooms Values("
    for i in arr:
        command += str(i)
        
        # For all elements except the last element
        if i != arr[len(arr) - 1]:
            command += ", " # Add the comma separator for the addition of values
        
    #for j in range(len(arr)):
        #command += str(arr[j])
    command += ") ON CONFLICT DO NOTHING"

    # Output will match: INSERT INTO table VALUES (Variable, Length, Values) ON CONFLICT DO NOTHING
    return command
    #INSERT INTO rooms VALUES(3, 'Bio', 202, 30, 'Classroom') ON CONFLICT DO NOTHING;

def insertCommandBuild(table, arr):
    table = str(table)
    command = "INSERT INTO " + table + " Values("
    for i in arr:
        command += str(i)
        
        # For all elements except the last element
        if i != arr[len(arr) - 1]:
            command += ", " # Add the comma separator for the addition of values
        
    #for j in range(len(arr)):
        #command += str(arr[j])
    command += ") ON CONFLICT DO NOTHING"
    
    '''if table == "rooms":
    elif table == "Class":
    elif table == "prof":'''
    
    # Output will match: INSERT INTO table VALUES (Variable, Length, Values) ON CONFLICT DO NOTHING
    return command

# Used in reading the schedule professor names
def flip(a):
    # If you have a zero
    if a == 0: 
        return 1 # Give back a one
    else: # Otherwise, you have a one
        return 0 # And should give back a zero
    

# Disassemble a line into its comma separated values
def scheduleRead(line, delimiter):
    temp = ""
    store = []
    profCheck = 0 # Initialize to not being a professor's name
    
    for i in line:
        if i == '"': # Clicks on and off based on quotation marks for reading the professor's name
            profCheck = flip(profCheck)

            
        if profCheck == 0: # If you're not dealing with a professor's name
            if i != delimiter:
                temp += i
            else:
                store.append(temp)
                temp = ""
        else:
            # You are reading a professor's name, currently
            temp += i
            #store.append(temp) # This will include the delimiter
            #temp = ""
            
    store.append(temp.strip()) # This is to account for the last string that does not have a comma after it
    return store

def roomRead(line, delimiter):
    temp = ""
    store = []

    for i in line:
        if i != delimiter:
            temp += i
        else:
            store.append(temp)
            temp = ""
    store.append(temp.strip()) # This is to account for the last string that does not have a comma after it
    return store



    
def sPrint(x):
    
    for i in x:
        s = ""
        for j in i:
            s += j + " "
        print(s)

# Extracts all columns of data in the CSV file data for schedule
def scheduleExtractor(sch):

    print("EXtracing schedule:\n ", sch)
    #DEPART = 0
    #COURSE_NUM = 1
    #COURSE_NAME = 2
    #XTRA = 3
    #SECTION = 4
    #INSTRUCTOR = 5
    #TIME = 6
    #CAP = 7

    departments = []
    course_nums = []
    course_names = []
    sec_names = []
    sections = []
    instructors = []
    times = []
    capacities = []

    for i in range(len(sch)):
        departments.append(sch[i][DEPART])
        course_nums.append(sch[i][COURSE_NUM])
        course_names.append(sch[i][COURSE_NAME])
        sec_names.append(sch[i][SEC_NAME])
        sections.append(sch[i][SECTION])
        instructors.append(sch[i][INSTRUCTORF])
        times.append(sch[i][TIME])
        capacities.append(sch[i][CAP])

    departments.pop(0)
    course_nums.pop(0)
    course_names.pop(0)
    sec_names.pop(0)
    sections.pop(0)
    instructors.pop(0)
    times.pop(0)
    capacities.pop(0)
    
    return departments, course_nums, course_names, sec_names, sections, instructors, times, capacities

def roomExtractor(rm):
    
    # ROOM = 0
    # CAPACITY = 1

    rooms = []
    capacities = []

    for i in range(len(rm)):
        rooms.append(rm[i][ROOM])
        capacities.append(rm[i][CAPACITY])

    if len(rooms) > 0:
        rooms.pop(0)
        capacities.pop(0)

    
    return rooms, capacities

def timePrep(times):

    errorCount = 0
    days = []
    time = []
    eTime = "0000"
    sTime = "0000"

    for i in times:
        if i[:3] == "MWF" or i[:3] == "mwf":
            days.append(MWF)
            sTime = str(i[3:])
            if len(sTime) > 2:
                eTime = str( int(sTime) + 50 )
            else:
                eTime = str( int(sTime)*100 + 50 )
        elif i[:2] == "mw" or i[:2] == "MW":
            days.append(MW)
            sTime = str(i[2:])
            if len(sTime) > 2:
                eTime = str( int(sTime) +115 )
            else:
                eTime = str( int(sTime)*100 + 115)
        elif i[:2] == "tt" or i[:2] == "TT":
            days.append(TT)
            sTime = str(i[2:])
            if len(sTime) > 2:
                eTime = str( int(sTime) + 115 )
            else:
                eTime = str( int(sTime)*100 + 115 )
        
        else:
            errorCount += 1
            print("Format error - dropped", errorCount, "from addition")
            days.append('00:00')
            time.append('00:00')

        print("StartTime ", sTime, " EndTime ", eTime, "\n")

        #sTime = str(i)
        
        #deciding the times in 00:00 format
        if(len(sTime) == 1): #ex: 4 o clock
            sh = "0" + sTime    
        elif(len(sTime) == 2): #ex: 10 o clock
            sh = sTime
        elif(len(sTime) == 3): #ex: 4:30/430
            sh = "0" + sTime[0]
            sm =  sTime[1:]
        elif(len(sTime) == 4): #ex: 1130
            sh = sTime[:1]
            sm = sTime[2:]
        else: 
            sh = "00"
            sm = "00" 

        if(len(eTime) == 1): #ex: 4 o clock
            eh = "0" + eTime
        elif(len(eTime) == 2): #ex: 10 o clock
            eh = eTime
        elif(len(eTime) == 3): #ex: 4:30/430
            eh = "0" + eTime[0]
            em = eTime[1:]
        elif(len(eTime) == 4): #ex: 1130
            eh = eTime[:1]
            em = eTime[2:]
        else: 
            eh = "00"
            em = "00" 

        if(int(sh) < 8 and int(sh) != 0): #this means it's pm and needs military time adjustment
            sh = str( int(sh) + 12) 
            eh = str( int(eh) + 12)

        time.append([sh+ ":"+sm,eh+":"+em])     

    return days, time


def nameFinder(names):
    specChars = [' ','"']
    firstName = ""
    lastName = ""
    fNameList = []
    lNameList = []
    comma = False

    for i in names: # For each name in the list

        firstName = ""
        lastName = ""
        comma = False
        for char in i:
            if char == ',':
                comma = True
            elif char in specChars:
                comma = comma
                # Do nothing because we don't want to add apostraphes
            else:
                if comma == False:
                    firstName += char
                else:
                    lastName += char

        fNameList.append(firstName)
        lNameList.append(lastName)

    return fNameList, lNameList


def nameFinderdbg(names):
    print(names)

    firstName = ""
    lastName = ""
    fNameList = []
    lNameList = []
    comma = False
    
    for i in names: # For each name in the list

        print(i)
        firstName = ""
        lastName = ""
        comma = False
        for char in i:
            print("Char = ",char)
            if char == ',':
                print("Comma found as:",char)
                comma = True
            else:
                if comma == False:
                    print("First:",firstName)
                    firstName += char
                    print("Added",firstName)
                else:
                    print("Last:",lastName)
                    lastName += char
                    print("Added",lastName)
                
        lNameList.append(firstName)
        fNameList.append(lastName)
        
    return fNameList, lNameList




def selectFile(self,fileName):
    #fileName = filedialog.askopenfilename()
    self.fileName = filedialog.askopenfilename()

def addFile(self,fileName,fileType):
    print("DEBUG: FILENAME: ", fileName)
    f = open(fileName,'r')
    #f.read()
    fType = fileType    #0 for room list, 1 for event list,see examples provided for format
    
    #parse data into proper fields, send to database
    times = []
    instructors = []
    
    if fType == 0: #reading class list
        print("CLASS LIST")
        buff = f.readlines()
        schedule = []
        for line in buff:
            print("i")
            schedule.append(scheduleRead(line, ','))
        print("The schedule: ", schedule)
        departments, course_nums, course_names, sec_names, sections, instructors, times, capacitiesS = scheduleExtractor(schedule)

        #setup times
        days, time = timePrep(times)
        print("TIMES\n\n", time)

        #code to add into database
        cursor.execute(DBqueries.queryClearAll)
        cursor.execute(DBqueries.queryLoadRooms)
        cursor.execute(DBqueries.queryLoadProf) 
        #Example:   
        #INSERT INTO events VALUES(1, 'Bio', '101', 10100, '10:00:00', '11:15:00', 'Generic Class', 1, 1) ON CONFLICT DO NOTHING;

        #Adding classes
        for i in range(len(departments)):
            #a complicated query to find an open room.
            roomIQuery = ("Select roomID from rooms where capacity >= " + str(capacitiesS[i]) + " and roomID not IN (SELECT roomID from events where '" 
            + str(time[i][0]) + ":00' <= endTime and '"+ str(time[i][0]) +":00' >= startTime) ORDER BY capacity desc LIMIT 1")
            cursor.execute(roomIQuery)
            try:
                roomIndex = cursor.fetchone()[0]
            except:
                print("No rooms")
            print("DEBUG ROOM IDEX: ", roomIndex)
            print("DEBUG roomIndex Query: \n", roomIQuery)

            query1 = ("INSERT INTO events VALUES("+ str(i) + " , '"+ str(course_names[i]) + "', '" + str(course_nums[i]) +"', " + str(days[i])+", "
            "'"+ str(time[i][0]) +":00', '" + str(time[i][1])  +":00', 'Generic Class', " + str(roomIndex) +", 1) ON CONFLICT DO NOTHING;"
            )
            if roomIndex == None:
                print("Room can't fit? ", query1)
            else:
                query1 = ("INSERT INTO events VALUES("+ str(i) + " , '"+ str(course_names[i]) + "', '" + str(course_nums[i]) +"', " + str(days[i])+", "
                "'"+ str(time[i][0]) +":00', '" + str(time[i][1])  +":00', 'Generic Class', " + str(roomIndex) +", 1) ON CONFLICT DO NOTHING;"
                )
                cursor.execute(query1)


    elif fType == 1: #reading room list
        print("Room lsit")
        buff = f.readlines()
        rm = []
        for line in buff:
            rm.append(roomRead(line, ','))
        rooms, capacitiesR = roomExtractor(rm)
        


    else:
        print("Incorrect file format requested")

        
    # All columns of data are now in their respective data arrays
    # Now, the next step will be using these arrays and their information to load the right tables with their respective elements and data

    days, time = timePrep(times)

    final_schedule = []
    final_rooms = []

    lnames, fnames = nameFinder(instructors)

    # Completely unnecessary to use but it is available if it facilitates anything
    #'''
    # for i in range(len(departments)):
    #     final_schedule.append([departments[i], course_nums[i], course_names[i], sec_names[i], sections[i], instructors[i], days[i], time[i], capacitiesS[i]])

    #for j in range(len(rooms)):
    #    final_rooms.append([rooms[j],capacitiesR[j]])


    ##############################################################
    #                     STATUS REPORT                          #
    ##############################################################
    #
    #      As of right now, the tables for the events file are:
    #      1. departments
    #      2. course_nums
    #      3. course_names
    #      4. sec_names
    #      5. sections
    #      6. instructors
    #      7. days
    #      8. time
    #      9. capacitiesS (The S behind capacities tells that this list of capacities is used for scheduling)
    #
    #      As of right now, the tables for the rooms file are:
    #      1. rooms
    #      2. capacitiesR (The R behind capacities tells that this list of capacities is used to input the room into the database)
    #

    ##############################################################
    #             HOW TO CONSTRUCT AN INSERT COMMAND             #
    ##############################################################
    #
    #      All related arrays have identical lengths and items 
    #      To build one insert command, take needed variables
    #      from all corresponding arrays using one index.
    #      For example,
    #
    #      'rooms' and 'capacitiesR' are related lists. To get
    #       a single row to be inserted and added, at row i in
    #       our data, we use rooms[i] and capacitiesR[i]. An example
    #       of how to get one single row of the rooms data is below.
    #
    #
    #
    #
    #
    #
    #
    # Simple example of setting up the insert command string to put into a query:
    #arr = []
    #index = 0
    #arr.append(rooms[index])
    #arr.append(capacitiesR[index])
    #print(insertRoomBuild(arr)) # Should print a valid insert command to the screen
    #
    #
    #
    #    
    #
    #      This works the exact same for the other related tables
    #      Professors need professor first name and last name when being inserted
    #          depending on the implementation of the database. This is how
    #          to structure the command.
    #
    #      Shape: INSERT INTO professors (firstName, lastName, any extra information)
    #
    #
    #    
    #arr = []
    #index = 10
    #arr.append(fnames[index])
    #arr.append(lnames[index])
    #print(insertCommandBuild("professor", arr))



    

