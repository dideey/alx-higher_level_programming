#!/usr/bin/python3
""" list all states from starting with N database hbtn_0e_0_usa using MySQLdb """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               password=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute('''SELECT * FROM states WHERE name LIKE 'N%'
                      ORDER BY states.id ''')
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    database.close()
