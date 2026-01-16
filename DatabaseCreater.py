import sqlite3

def create():
    conobj=sqlite3.connect(database="mybank.sqlite")
    curobj=conobj.cursor()
    query="""
        CREATE TABLE IF NOT EXISTS accounts(
        account INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        mobile TEXT,
        email TEXT,
        aadhar TEXT,
        balance REAL,
        opendate TEXT)
"""
    curobj.execute(query)
    conobj.close()
