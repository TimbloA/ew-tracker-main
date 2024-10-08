import sqlite3

class Database:
    def __init__(self, url):
        self.url = url
        with sqlite3.connect(self.url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                beak TEXT NOT NULL,
                subject TEXT NOT NULL,
                dueDate TEXT NOT NULL
            );
            """
            cursor.execute(sql)
            db.commit()

    def create_ew(self, task, beak, subject, dueDate):
       
        with sqlite3.connect(self.url) as db:
            cursor = db.cursor()
            sql_insert = """
            INSERT INTO ew (task, beak, subject, dueDate) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, (task, beak, subject, dueDate))
            db.commit()

    def get_ews(self):
        with sqlite3.connect(self.url) as db:
            cursor = db.cursor()
            sql = "SELECT id, task, beak, subject, dueDate FROM ew;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            tasks = [{'id': row[0], 'task': row[1], 'beak': row[2], 'subject': row[3], 'due_date': row[4]} for row in rows]
            return tasks
   

   



    # EXTRA CREDIT
    def get_ew(self, task):
        pass