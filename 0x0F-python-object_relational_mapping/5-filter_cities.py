#!/usr/bin/python3
""" This module intergrates MySQL into Python."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    arg =  argv[4]

    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cur = db.cursor()

    qry = """
    SELECT cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id;
    """

    cur.execute(qry)

    rows = cur.fetchall()
    out = ""
    for col0, col1 in rows:
        if col1 == arg:
            out += f"{col0}, "
    print(out.strip(", "))

    cur.close()
    db.close()
