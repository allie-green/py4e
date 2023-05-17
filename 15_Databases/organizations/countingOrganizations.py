import sqlite3

connection = sqlite3.connect('orgsDB.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('ENTER FILE NAME: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    organization = email.split("@")[1]

    # Select the column named 'count'
    # where the value in the 'org' column matches the value of the organization variable
    # (?) is a placeholder for the value of organization
    cursor.execute('SELECT count FROM Counts WHERE org = ?', (organization,))

    # Retrieve the row returned by the previous SQL query
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organization,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (organization,))
    # The changes are committed/written to the table
    connection.commit()

# The rest is not committed to the table, but we execute one last command to print the results in the terminal.
first10 = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(first10):
    print(str(row[0]), row[1])

cursor.close()