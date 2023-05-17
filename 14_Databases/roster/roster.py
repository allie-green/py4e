import json
import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Drop existing tables if they exist and create new tables for User and Course
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
''')

# Create a table for Member that relates Users and Courses
# The primary key is a combination of user_id and course_id
cur.executescript('''
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Prompt the user for the file name, default to 'roster_data_sample.json'
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# Read the JSON data from the file
str_data = open(fname).read()
json_data = json.loads(str_data)

# Iterate over each entry in the JSON data
for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2] # 1 for instructor, 0 for student.

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    # Insert or replace the Member relationship into the Member table
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )
    
    conn.commit()

# Close the database connection
cur.close()