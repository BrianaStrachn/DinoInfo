#Use python to create a database of apartment-pet info

import sqlite3
import csv

conn = sqlite3.connect('Dino.db')
c = conn.cursor()


data_in = open('allDinoNew.csv','r')
data_reader = csv.reader(data_in)

column_headers = data_reader.next()

for row in data_reader:
	c.execute('INSERT INTO Dinosaur VALUES(?,?,?,?)',row)


conn.commit()
conn.close()
data_in.close()