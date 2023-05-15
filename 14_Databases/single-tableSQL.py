import sqlite3

# Connect to the database or create a new one if it doesn't exist
connection = sqlite3.connect('ages.sqlite')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Drop (deletes the table from the db) if it already exists.
# This done to allow us to run the same program to create the Ages without causing an error.
cursor.execute('DROP TABLE IF EXISTS Ages')

# Create the Ages table with name and age columns
cursor.execute('CREATE TABLE Ages (name TEXT, age INTEGER)')

# Function to insert a new row into the Ages table
def insert(name, age):
    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', (name, age))

# Insert sample data into the table
insert('Olaoluwapolorimi', 13)
insert('Maryse', 19)
insert('Alyx', 29)
insert('Zakariya', 19)
insert('Lybi', 16)

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()