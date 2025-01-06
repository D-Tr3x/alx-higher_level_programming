#!/usr/bin/python3
"""
Module lists all `cities` from `hbtn_0e_usa` database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
