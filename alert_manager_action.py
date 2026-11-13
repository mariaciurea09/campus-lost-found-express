import sqlite3


class AlertManagerAction:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path

    def execute(self, new_item_title, new_item_category):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT user_contact FROM alerts WHERE category = ? AND ? LIKE '%' || keyword || '%'",
            (new_item_category, new_item_title)
        )
        alerts = cursor.fetchall()
        conn.close()

        notifications = [row[0] for row in alerts]
        return notifications