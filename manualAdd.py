###
# Created on Apr 6,2020
#
# @author: Brady Ronayne
# Manages manual input for classes
###

import psycopg2
import psycopg2.extensions
import os
import DBqueries

connection = psycopg2.connect(user = "postgres",
                                  password = "software447",
                                  host = "database447.cst3jimtz2ge.us-east-2.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ClassScheduler")

                                  
#setup database
connection.autocommit = True
cursor = connection.cursor()

def manualInputRoom(name, number, capacity):

    
        nextID = 1
        #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
        try:
                cursor.execute(DBqueries.findIndexRooms)
                nextID = int(cursor.fetchone()[0] ) + 1 #next index
        except:
                print("", end = "") #just a blank except
        query1 = "INSERT INTO rooms VALUES("+str(nextID)+", '"+ str(name.get()) + "', '" + str(number.get()) + "', " + str(capacity.get()) + ", 'Classroom') ON CONFLICT DO NOTHING;"
        cursor.execute(query1)

def manualInputEvent(subject, courseNum, time, instructor):

        #cursor.execute(DBqueries.queryLoadProf)

        nextID = 1
        #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
        cursor.execute(DBqueries.findIndexEvents)
        try:
                nextID = int(cursor.fetchone()[0] ) + 1 #next index
        except:
                print("", end = "") #blank except statement

        try:
                query1 = "INSERT INTO events VALUES("+str(nextID)+", '"+ str(subject.get()) + "', '" + str(courseNum.get()) + "', 10101, '" + str(time.get()) + "', '11:15:00', 'Class from UI', " + str(instructor.get()) +", 1) ON CONFLICT DO NOTHING;"
                cursor.execute(query1)
        except:
                query1 = "INSERT INTO events VALUES("+str(nextID)+", '"+ str(subject.get()) + "', '" + str(courseNum.get()) + "', 10101, '10:00:00', '11:15:00', 'Class from UI', " + str(instructor.get()) +", 1) ON CONFLICT DO NOTHING;"
                cursor.execute(query1)
        