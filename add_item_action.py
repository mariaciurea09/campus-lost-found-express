import sqlite3
from item_model import ItemModel
from datetime_service import DateTimeService


class AddItemAction:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path
        self.time_api = DateTimeService()

    def execute(self, title, category, location):
        if not title or title.strip() == "":
            raise ValueError("Eroare: Titlul obiectului nu poate fi gol.")

        # Preluare dată și oră automată prin API
        current_date_time = self.time_api.get_current_time()

        item = ItemModel(title, category, location, current_date_time)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (title, category, location, date_time, status) VALUES (?, ?, ?, ?, ?)",
            (item.title, item.category, item.location, item.date_time, item.status)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        return new_id