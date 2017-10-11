import sqlite3 as lite
import sys

con - lite.connect('user.db')

with con:
    cur = con.cursor()
    cur execute("CRETE ")