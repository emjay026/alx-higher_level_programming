#!/usr/bin/python3
""" This module intergrates MySQL into Python."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    arg = argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("""
    SELECT *
    FROM states
    WHERE name = %s
    ORDER BY id;
    """, (arg,))

    rows = cur.fetchall()

    for col0, col1 in rows:
        print(f"({col0}, '{col1}')")
