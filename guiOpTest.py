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

#def rebuild()


def searchDB(self, keywords,searchRooms,searchEvents):
    #search db based on keywords
    #search rooms for keywords if searchRooms = 1
    #search events for keywords is searchEvents = 1
    #place correct itmes in roomList
    roomList = []
    print ("DEBUG: ", searchEvents.get())

    #TESTING
    idList = []
    searchKeywords = str(keywords.get()).split()
    if str(keywords.get()) == "" or searchRooms.get() == 0:
        query1 = "select roomid, building, roomnum, capacity from rooms"
        cursor.execute(query1)
    elif searchRooms.get() == 1:
        if(len(searchKeywords) > 1):
            query1 = "select roomid, building, roomnum, capacity from rooms where CAST (roomnum AS text) ILIKE '%" + searchKeywords[0] + "' and building ILIKE '%" + searchKeywords[1] + "%'"
            cursor.execute(query1)
            for roomid, building, roomnum, capacity in cursor.fetchall():
                roomList.append(Room(building, str(roomnum) , str(capacity)) )
                idList.append(roomid)
            query2 = "select roomid, building, roomnum, capacity from rooms where CAST (roomnum AS text) ILIKE '%" + searchKeywords[1] + "%' and building ILIKE '%" + searchKeywords[0] + "%'"
            cursor.execute(query2)
            #cursor.execute(query1)
        else:
            query1 = "select roomid, building, roomnum, capacity from rooms where CAST (roomnum AS text) ILIKE '%" + searchKeywords[0] + "%' or building ILIKE '%" + searchKeywords[0] + "%'"
            cursor.execute(query1)

    for roomid, building, roomnum, capacity in cursor.fetchall():   
        roomList.append(Room(building, str(roomnum) , str(capacity)) )
        idList.append(roomid)
    #end testing

    # if(len(searchKeywords) > 1):
    #     query1 = "select roomid, building, roomnum, capacity from rooms where CAST (roomnum AS text) = '" + searchKeywords[1] + "' or building = '" + searchKeywords[1] + "'"
    #     cursor.execute(query1)

    #     for roomid, building, roomnum, capacity in cursor.fetchall():
    #         roomList.append(Room(building, str(roomnum) , str(capacity)) )
    #         idList.append(roomid)
    #     #end testing

    # j = 1
    # cursor2 = connection.cursor()
    # for i in range(len(roomList)):
    #     if searchEvents.get() == 1:
    #         if len(searchKeywords) > 1:
    #             query1 = "Select resID, eventName, courseNum, profID from events where roomID = " + str(idList[i]) + " AND ( eventName ILIKE '%" + searchKeywords[0] + "%' OR eventName ILIKE '%" + searchKeywords[1] + "%' )"
    #         else:
    #             query1 = "Select resID, eventName, courseNum, profID from events where roomID = " + str(idList[i]) + " AND eventName ILIKE '%" + keywords.get() + "%'"
    #     else:
    #         query1 = "Select resID, eventName, courseNum, profID from events where roomID = " + str(idList[i])
    #     cursor2.execute(query1)
    #     for resID, eventName, courseNum, profID in cursor2.fetchall():
    #         roomList[i].addEvent(j,Events(eventName, courseNum," ","02",profID,"TTH1",50))
    #         j += 1 #index for adding events

    #Code to add events within the room
    j = 1
    cursor2 = connection.cursor()
    for i in range(len(roomList)):
        if searchEvents.get() == 1:
            if len(searchKeywords) > 1:
                query1 = "Select resID, eventName, courseNum, profID, startTime from events where roomID = " + str(idList[i]) + " AND ( eventName ILIKE '%" + searchKeywords[0] + "%' OR eventName ILIKE '%" + searchKeywords[1] + "%' )"
            else:
                query1 = "Select resID, eventName, courseNum, profID, startTime from events where roomID = " + str(idList[i]) + " AND eventName ILIKE '%" + keywords.get() + "%'"
        else:
            query1 = "Select resID, eventName, courseNum, profID, startTime from events where roomID = " + str(idList[i])
        cursor2.execute(query1)
        j = 1
        for resID, eventName, courseNum, profID, startTime in cursor2.fetchall():
            timeSlot = (int(str(startTime)[:2]) - 8)*2 // 1
            roomList[i].addEvent(timeSlot,Events(str(startTime)[:4] +"-" + str(timeSlot), courseNum," ","02",profID,"TTH" + str(timeSlot) ,50))
            j += 1 #index for adding events


    return roomList