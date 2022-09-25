import sqlite3

#Connecting to sqlite3 using connect method in sqlite3 module
connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#Craeting a new Table with name Movies
cursor.execute('Create Table Movies (name text, actor text, actress text, director text, year_of_release integer)')

#data to be stored
data = [
    ('In the Mood for Love','Tony Leung','Maggie Cheung','Wong Kar-wai',2000),
    ('Eternal Sunshine of the Spotless Mind','Jim Carrey','Kate Winslet','Micheal Gondry',2004),
    ('The Science of Sleep','Gael García Bernal','Charlotte Gainsbourg','Micheal Gondry',2006),
    ('Fight Club','Brad Pitt','Helena Bonham','David Fincher',1999),
    ('Se7en','Ben Affleck','Rosamund Pike','David Fincher',2014),
    ('The Mask','Jim Carrey','Camron Diaz','Chuck Russel',1994),
    ('The Majestic','Jim Carrey','Laurie Holden','Frank Darabont',2001),
    ('The Wolf of Wall Street','Leonardo DiCaprio','Margot Robbie','Martin Scorsese',2013),
    ('Shutter Island','Leonardo DiCaprio','Emily Mortimer','Martin  Scorsese',2010),
    ('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolan',2010),
]

#inserting all the rows at once
cursor.executemany("insert into Movies values (?,?,?,?,?)", data)

#commting the changes to the database
connection.commit()

#function to print all the rows
def print_all_rows():
    for row in cursor.execute("select * from Movies"):
        print(row)

#function to print Lead actor specific movies
def print_actor_movies(hero):
    print("**********",hero,"Movies***********")
    for row in cursor.execute("select * from Movies where actor=:h",{"h":hero}):
        print(row)

#function to print Director specific movies
def print_director_movie(director):
    print("**********",director,"Movies***********")
    for row in cursor.execute("select * from Movies where director=:d",{"d":director}):
        print(row)



print_all_rows()
print_actor_movies("Leonardo DiCaprio")
print_director_movie("Micheal Gondry")

#closing the connection
connection.close()