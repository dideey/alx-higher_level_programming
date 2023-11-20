#!/bin/bash/python3
"""listing all states begining with N"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost"user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(row) for row in cursor.fetchall() if row[1][0] == "N"]
    cursor.close()
    db.close()
