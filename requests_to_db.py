# coding: utf-8

import sqlite3
import psycopg2

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cursor = conn.cursor()

# Read
cursor.execute('SELECT Name FROM Artist ORDER BY Name LIMIT 3')

results = cursor.fetchall()
results2 = cursor.fetchall()

print results  # [(u'A Cor Do Som',), (u'AC/DC',), (u'Aaron Copland & London Symphony Orchestra',)]
print results2  # []

# Write
cursor.execute('INSERT INTO Artist VALUES (Null, "A nasty!")')
conn.commit()  # in case of changin DB

cursor.execute('SELECT Name FROM Artist ORDER BY Name LIMIT 3')
results = cursor.fetchall()
print results

# Placeholder

# C подставновкой по порядку на места знаков вопросов:
print cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", '2').fetchall()

# И с использованием именнованных замен:
print cursor.execute("SELECT Name from Artist ORDER BY Name LIMIT :limit", {"limit": 3}).fetchall()

print cursor.execute("SELECT Name FROM ? ORDER BY Name LIMIT 2", 'Artist').fetchall()  # Error

# Many and Iterator

new_artists = [
    ('A aa',),
    ('A a2',),
    ('A a3',)
]
cursor.executemany('INSERT INTO Artist VALUES (Null, ?);', new_artists)
cursor.execute('SELECT Name FROM Artist ORDER BY Name LIMIT 3')
print cursor.fetchone()
print cursor.fetchone()
print cursor.fetchone()

for row in cursor.execute('SELECT Name from Artist ORDER BY Name LIMIT 3'):
    print row

conn.close()

connect = psycopg2.connect(database='test_base', user='test_user', host='localhost', password='test_password')
cursor = connect.cursor()

cursor.execute("CREATE TABLE tbl(id INT, data JSON);")

cursor.execute('INSERT INTO tbl VALUES (1, \'{ "name":"Tester" }\');')
connect.commit()

cursor.execute("SELECT * FROM tbl;")
for row in cursor:
    print(row)

connect.close()
