import sqlite3
from datetime import datetime
from openai import OpenAI

class ThreadDB:
    def __init__(self, db_name='../output/threads.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        Create the database table if it doesn't exist.
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS threads (
            id INTEGER PRIMARY KEY,
            thread_id TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()

    def add_thread(self, thread_id):
        """
        Add a new thread to the database.
        """
        self.cursor.execute('''
        INSERT INTO threads (thread_id)
        VALUES (?)
        ''', (thread_id,))
        self.conn.commit()

    def get_all_threads(self):
        """
        Retrieve all threads from the database.
        """
        self.cursor.execute('SELECT * FROM threads')
        return self.cursor.fetchall()

    def find_thread_by_id(self, thread_id):
        """
        Find a specific thread by its ID.
        """
        self.cursor.execute('SELECT * FROM threads WHERE thread_id = ?', (thread_id,))
        return self.cursor.fetchone()

    def remove_thread_by_id(self, thread_id):
        """
        Remove a specific thread by its ID.
        """
        self.cursor.execute('DELETE FROM threads WHERE thread_id = ?', (thread_id,))
        self.conn.commit()
        response = OpenAI().beta.threads.delete(thread_id)
        print(response)

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()