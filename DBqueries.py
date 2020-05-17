###
# Created on Apr 8,2020
#
# @author: Brady Ronayne
# Sample and useful queries (postgreSQL)
###

findIndexRooms = """
select MAX(roomID) from rooms;
"""
findIndexEvents = """
select MAX(resID) from events;
"""

queryClearEvents = """
DROP TABLE IF EXISTS classes CASCADE ;
DROP TABLE IF EXISTS events CASCADE;
CREATE TABLE events (
	resID integer NOT NULL,
	eventName varchar(30),
	courseNum varchar(30), --this can be a string, might be “100L”
	days int, -- days of the week as binary - 10101 (mwf) 
	startTime time,
	endTime time,
	classInfo text,
	roomID integer NOT NULL,
	profID integer,
	FOREIGN KEY (roomID) REFERENCES rooms (roomID) ON DELETE CASCADE,
	FOREIGN KEY (profID) REFERENCES prof (profID) ON DELETE CASCADE,
	PRIMARY KEY (resID)
);
"""

queryLoadEvents = """
INSERT INTO events VALUES(1, 'Bio', '101', 10100, '10:00:00', '11:15:00', 'Generic Class', 1, 1) ON CONFLICT DO NOTHING;

INSERT INTO events VALUES(2, 'CMSC', '447', 10100, '10:00:00', '11:15:00', 'Generic Class', 1, 1) ON CONFLICT DO NOTHING;

INSERT INTO events VALUES(3, 'Math', '112L', 10100, '10:00:00', '11:15:00', 'Generic Class', 4, 1) ON CONFLICT DO NOTHING;

INSERT INTO events VALUES(4, 'Bio', '201', 10100, '10:00:00', '11:15:00', 'Generic Class', 3, 1) ON CONFLICT DO NOTHING;

INSERT INTO events VALUES(5, 'Bio', '301', 10100, '10:00:00', '11:15:00', 'Generic Class', 3, 1) ON CONFLICT DO NOTHING;
"""

queryClearAll = """
DROP TABLE IF EXISTS rooms CASCADE;
CREATE TABLE rooms (
	roomID integer NOT NULL,
	building text,
	roomNum integer,
	capacity integer,
	roomType varchar(30),
	PRIMARY KEY (roomID)
);

DROP TABLE IF EXISTS prof CASCADE ;
CREATE TABLE prof (
	profID integer NOT NULL,
	fName varchar(40),
	lName varchar(40),
	allergies varchar(40),
	website varchar(40),
	information text,
	PRIMARY KEY (profID)
);

DROP TABLE IF EXISTS classes CASCADE ;
DROP TABLE IF EXISTS events CASCADE;
CREATE TABLE events (
	resID integer NOT NULL,
	eventName text,
	courseNum varchar(30), --this can be a string, might be “100L”
	days int, -- days of the week as binary - 10101 (mwf) 
	startTime time,
	endTime time,
	classInfo text,
	roomID integer NOT NULL,
	profID integer,
	FOREIGN KEY (roomID) REFERENCES rooms (roomID) ON DELETE CASCADE,
	FOREIGN KEY (profID) REFERENCES prof (profID) ON DELETE CASCADE,
	PRIMARY KEY (resID)
);

"""

queryLoadRooms = """
INSERT INTO rooms VALUES(1, 'ILSB', 118, 30, 'Classroom') ON CONFLICT DO NOTHING;
INSERT INTO rooms VALUES(2, 'Chem', 30, 200, 'Classroom') ON CONFLICT DO NOTHING;

INSERT INTO rooms VALUES(3, 'Bio', 202, 30, 'Classroom') ON CONFLICT DO NOTHING;

INSERT INTO rooms VALUES(4, 'ITE', 201, 60, 'Classroom') ON CONFLICT DO NOTHING;

INSERT INTO rooms VALUES(5, 'Math', 202, 30, 'Classroom') ON CONFLICT DO NOTHING;

INSERT INTO rooms VALUES(6, 'Math', 301, 30, 'Classroom') ON CONFLICT DO NOTHING;


"""

queryLoadProf = """
INSERT INTO prof VALUES(1, 'John', 'Smith', 'Chalk Allergy', 'www.website.com', 'A generic teacher, hates chalk, talks loudly, students still fall asleep' ) ON CONFLICT DO NOTHING;
"""

import psycopg2
import psycopg2.extensions
import os

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

#INSERT INTO prof VALUES(1, 'John', 'Smith', 'Chalk Allergy', 'www.website.com', 'students fall asleep' ) ON CONFLICT DO NOTHING;
#A function that returns the professor ID of a professor and adds it if necessary
def findProfessor( lastName, name):
	print("BRUH THIS FUNCTION")
	returnID = 1
	cursor.execute("Select profID from prof where fName ILIKE '%" + name + "%' and lName ILIKE '%" + lastName + "%' ")
	try:
		returnID = cursor.fetchone()[0]
	except:
		print("EXCEPT?")
		index = 1
		try:
			index = 1 + cursor.execute("select MAX(profID) from prof;")
		except:
			print("First Professor (likely)")
		cursor.execute("INSERT INTO prof VALUES("+ str(index)+ ", '" + name+"', '" + lastName+"', 'Chalk Allergy', 'www.website.com', 'students fall asleep' ) ON CONFLICT DO NOTHING;")
		print("ADDED PROF#: ", index)
		return index
	print("BRUHHHH")
	return returnID
