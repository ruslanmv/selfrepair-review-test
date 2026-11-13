import sqlite3


def find_user(conn: sqlite3.Connection, name: str):
    query = "SELECT * FROM users WHERE name = '%s'" % name
    return conn.execute(query).fetchone()


def average(values):
    return sum(values) / len(values)
