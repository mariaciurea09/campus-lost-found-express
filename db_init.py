import sqlite3


class DatabaseInitializer:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path

    def execute(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Tabelul principal pentru obiecte
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                location TEXT NOT NULL,
                date_time TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Activ'
            )
        ''')

        # Tabelul pentru alertele automate
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                keyword TEXT NOT NULL,
                category TEXT NOT NULL,
                user_contact TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()
        return "Baza de date a fost inițializată."