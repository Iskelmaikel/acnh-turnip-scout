import sqlite3
import time


def setup_db():
    # Create a db if it doesn't yet exist. Opens it up too
    db = sqlite3.connect('data/turnip_database')
    # Get a cursor object
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE if not exists turnips(name TEXT, datetime TEXT, dodocode TEXT)
    ''')
    # for debug purposes: Add row
    #cursor.execute('''INSERT INTO turnips(name, datetime, dodocode) VALUES(?,?,?)''', ('first entry', 'utc now', 'ABCDE'))
    db.commit()


def get_turnips():
    print('Fetching turnips')
    db = sqlite3.connect('data/turnip_database')
    cursor = db.cursor()
    cursor.execute('''SELECT name, datetime, dodocode FROM turnips''')
    all_rows = cursor.fetchall()
    return all_rows


def does_turnip_exist(name):
    db = sqlite3.connect('data/turnip_database')
    cursor = db.cursor()
    cursor.execute('''SELECT name, datetime, dodocode FROM turnips WHERE name = ?''', (name,))
    all_rows = cursor.fetchall()
    return len(all_rows)


def add_turnips(name, datetime, dodocode):
    exists = does_turnip_exist(name)

    if exists > 0:
        print('Already in db. Skipping ' + name)
        return 'false'

    print('Adding turnips entry to db')

    db = sqlite3.connect('data/turnip_database')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO turnips(name, datetime, dodocode) VALUES(?,?,?)''', (name, datetime, dodocode))
    db.commit()
    return 'true'