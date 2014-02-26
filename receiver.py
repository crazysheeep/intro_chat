#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
import sqlite3
import pickle
import datetime
import time

postvars = cgi.FieldStorage()
# postvars = {}
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

# postvars["user"] = "test"
# postvars["message"] = "test"
newMessage = {"user": postvars["user"], "message": postvars["message"], "timestamp": datetime.datetime.now()}
cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage),))

time.sleep(0.1) # to get greater timestamp
newMessage2 = {"user": "pythonbot", "message": "{} is a retard".format(postvars["user"]), "timestamp": datetime.datetime.now()}
cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage2),))

connection.commit()
connection.close()

print("Content-type:text/plain\n")
print("success")
