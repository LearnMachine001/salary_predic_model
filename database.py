import sqlite3

conn = sqlite3.connect("salary_predict.db")


cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id REAL PRIMARY KEY AUTOINCREMENT ,
        name TEXT NOT NULL DEFAULT "UNKNOWN",
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL)
        
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS prediction(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                experience REAL NOT NULL DEFAULT 0,
                predicted_salary REAL NOT NULL)
                ''')


conn.commit()

conn.close()
print("Table created successfully ")


