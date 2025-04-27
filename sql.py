import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Create the table (only if it doesn't already exist)
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rajesh', 'Data Science', 'A',100)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sindhu', 'Data Science', 'B',84)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudha', 'DEVOPS', 'C',64)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'D',50)''')

# Display all the records
print("The inserted records are:")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Commit the changes
connection.commit()

# Close the connection
connection.close()
