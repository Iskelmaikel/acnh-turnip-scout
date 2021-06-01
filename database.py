import sqlite3
import time


DB_PATH = 'data/turnip_submissions.db'


def setup_db():
    print('[DB] Setting up database')
    db = sqlite3.connect(DB_PATH)
    # Get a cursor object
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE if not exists submissions(id TEXT PRIMARY KEY, title TEXT, created TEXT, shortlink TEXT)
    ''')
    db.commit()


def get_submissions():
    print('[DB] Fetching all submissions')
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM submissions''')
    return cursor.fetchall()


def does_submission_exists(id):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM submissions WHERE id = ?''', (id,))
    all_rows = cursor.fetchall()
    return True if len(all_rows) > 0 else False


def add_submission(sub):
    if not does_submission_exists(sub.id):
        print("[DB]({id}) - Adding to db".format(id=sub.id))
        db = sqlite3.connect(DB_PATH)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO submissions(id,title,created,shortlink) VALUES(?,?,?,?)''', (sub.id,sub.title,sub.created_utc,sub.shortlink))
        db.commit()
        return True
    else:
        print("[DB]({id}) - Submission already exists in db".format(id=sub.id))
        return False