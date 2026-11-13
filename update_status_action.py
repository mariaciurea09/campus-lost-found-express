import sqlite3


class UpdateStatusAction:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path

    def execute(self, item_id, new_status="Recuperat"):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE items SET status = ? WHERE id = ?",
            (new_status, item_id)
        )
        affected_rows = cursor.rowcount
        conn.commit()
        conn.close()

        if affected_rows == 0:
            raise ValueError(f"Eroare: Obiectul cu ID-ul {item_id} nu a fost găsit.")
        return f"Obiectul {item_id} a fost marcat ca {new_status}."