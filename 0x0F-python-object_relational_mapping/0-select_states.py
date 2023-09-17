#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cur = db.cursor()
    cur.execute(f"USE {database_name}")
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()

    for col0, col1 in rows:
        print(f"({col0}, '{col1}')")
