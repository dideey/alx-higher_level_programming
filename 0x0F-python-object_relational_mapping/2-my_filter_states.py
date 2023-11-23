#!/usr/bin/python3
""""""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               password=sys.argv[2], db=sys.argv[3], port=3306)
    search = sys.argv[4]
    cursor = database.cursor()
    cursor.execute('''SELECT * FROM states WHERE name LIKE
                   '{}' ORDER BY states.id'''.format(search))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()
