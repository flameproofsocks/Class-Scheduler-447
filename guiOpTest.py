from Room import Room
from Events import Events

import psycopg2
import psycopg2.extensions
import os

connection = psycopg2.connect(user = "postgres",
                                  password = "software447",
                                  host = "database447.cst3jimtz2ge.us-east-2.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ClassScheduler")

                                  
#setup database
connection.autocommit = True
cursor = connection.cursor()

def searchDB(self, keywords,searchRooms,searchEvents):
    #search db based on keywords
    #search rooms for keywords if searchRooms = 1
    #search events for keywords is searchEvents = 1
    #place correct itmes in roomList
    roomList = []

    #TESTING
    
    query1 = "select roomid, building, roomnum, capacity from rooms where roomnum = " + str(keywords.get())
    cursor.execute(query1)

    idList = []
    for roomid, building, roomnum, capacity in cursor.fetchall():
        roomList.append(Room(building, str(roomnum) , str(capacity)) )
        idList.append(roomid)
    #end testing

    j = 1
    cursor2 = connection.cursor()
    for i in range(len(roomList)):
        query1 = "Select resID, eventName, courseNum, profID from events where roomID = " + str(idList[i]) 
        cursor2.execute(query1)
        for resID, eventName, courseNum, profID in cursor2.fetchall():
            roomList[i].addEvent(j,Events(eventName, courseNum," ","02",profID,"TTH1",50))
            j += 1 #index for adding events

    return roomList