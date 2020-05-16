import psycopg2
import psycopg2.extensions
import os
import DBqueries

# connection = psycopg2.connect(user = "postgres",
#                                   password = "bippy",
#                                   host = "localhost",
#                                   port = "5432",
#                                   database = "447ver1")

connection = psycopg2.connect(user = "postgres",
                                  password = "software447",
                                  host = "database447.cst3jimtz2ge.us-east-2.rds.amazonaws.com",
                                  port = "5432",
                                  database = "ClassScheduler")

                                  
#setup database
connection.autocommit = True
cursor = connection.cursor()

def manualInputRoom():

    

        #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
        cursor.execute(DBqueries.findIndexRooms)
        nextID = int(cursor.fetchone() ) + 1 #next index
        query1 = "INSERT INTO rooms VALUES("+str(nextID)+", '"+ str(window1.entry_addRoom_name.get()) + "', '" + str(window1.entry_addRoom_number.get()) + "', 30, 'Classroom') ON CONFLICT DO NOTHING;"
        cursor.execute(query1)

def manualInputEvent(subject, courseNum, instructor):

        #query1 = "select building, roomnum from rooms where building = '" + window1.entry_search_building.get() + "' AND roomnum = '" + window1.entry_search_num.get() + "'"
        cursor.execute(DBqueries.findIndexEvents)
        nextID = int(cursor.fetchone()[0] ) + 1 #next index
        query1 = "INSERT INTO events VALUES("+str(nextID)+", '"+ str(subject.get()) + "', '" + str(courseNum.get()) + "', 10101, '10:00:00', '11:15:00', 'Class from UI', " + str(instructor.get()) +", 1) ON CONFLICT DO NOTHING;"
        cursor.execute(query1)