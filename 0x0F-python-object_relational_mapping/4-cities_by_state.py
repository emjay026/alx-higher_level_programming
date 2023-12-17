#!/usr/bin/python3
""" This module intergrates MySQL into Python."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    if len(argv) != 4:
        exit()

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
    """)

    rows = cur.fetchall()

    for col0, col1, col3 in rows:
        print(f"({col0}, '{col1}', '{col3}')")

    cur.close()
    db.close()
