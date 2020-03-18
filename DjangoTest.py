import django
print(django.get_version())
#import django

import psycopg2
import psycopg2.extensions
import os

connection = psycopg2.connect(user = "postgres",
                                  password = "bippy",
                                  host = "localhost",
                                  port = "5432",
                                  database = "447ver1")
#setup database
connection.autocommit = True
cursor = connection.cursor()

# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

query1 = "SELECT * FROM rooms"
cursor.execute(query1)
for table in cursor.fetchall():
    print(table)

#A test of django.
#Stuff

