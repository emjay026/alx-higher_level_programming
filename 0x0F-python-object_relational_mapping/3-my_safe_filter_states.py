#!/usr/bin/python3
""" This module intergrates MySQL into Python."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    arg_draft = argv[4]

    kwrds = [",", "'", " ", "SELECT", "TRUNCATE", "TABLE", "FROM",
             "WHERE", "LIKE", "USER", "SHOW", "INSERT", "DELETE"]

    arg_split = arg_draft.split(';')

    for a in kwrds:
        arg_split[0] = arg_split[0].replace(a, "")

    arg_final = arg_split[0]

    db = MySQLdb.connect(host='localhost',
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cur = db.cursor()

    qry = """
    SELECT *
    FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id ASC;
    """.format(arg_final)

    cur.execute(qry)

    rows = cur.fetchall()
    for col0, col1 in rows:
        print(f"({col0}, '{col1}')")

    cur.close()
    db.close()
