import sqlite3
import csv
import wikipedia as w

conn = sqlite3.connect('Dino.db')
c = conn.cursor()

def Char():
  c.execute('SELECT * FROM Characteristic JOIN Dinosaur ON (SELECT Characteristic_ID FROM ID_Info WHERE ID = Dinosaur.ID) LIMIT(10);')
  print('So here are a few Dinosaurs with their Names, Taxonomy, Type_Species, Weight in kg, their type of teeth, how it moved, and their length in meters.')


def Menu():
  print(w.summary('Dinosaurs', sentences = 4))
  DinoInfo = 'l'
  while DinoInfo!='e':
    print('''
    Hello Prehistoric Explorers! Millions of years ago, huge 
    beings known as Dinosaurs used to roam this land. As time has passed
    and these animals have gone extinct, more and more information about
    these wondourous animals have been collected. YOU now have the chance 
    to learn in depth about different Dinosaurs! Choose from the options 
    below on what you would like to learn today:
    
    a.  Learn about certain Dinosaurs and their characteristics!
    b. What kind of diet do certain Dinosaurs follow?
    c. What's going on with these Dinosaur names and where were these Dinos found?
    d. Lets learn about the period where these Dinos came from!
    e. I DONT LIKE DINOS! LET ME LEAVE TO GET COFFEE!
    
    To choose, type either a, b, c, d, or e.
    ''')
    DinoInfo = raw_input('What is your choice for today? ').lower()
    if DinoInfo == 'a':
      Char()
    elif DinoInfo == 'e':
     quit()
    else:
     print('RAWR! DO YOU NOT KNOW HOW TO READ OR DO YOU NEED GLASSES? CHOOSE A VALID CHOICE OR GET LOST!') 



Menu()
conn.commit()
conn.close()
#data_in.close()

