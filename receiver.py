#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
import sqlite3
import pickle
import datetime

postvars = cgi.FieldStorage()
postvars = {}
connection = sqlite3.connect("messages.db")
cursor = connection.cursor()

postvars["user"] = "test"
postvars["message"] = "test"
newMessage = {"user": postvars["user"], "message": postvars["message"], "timestamp": datetime.datetime.now()}

cursor.execute("INSERT INTO messages VALUES(?);", (pickle.dumps(newMessage),))
connection.commit()
connection.close()

print("success")