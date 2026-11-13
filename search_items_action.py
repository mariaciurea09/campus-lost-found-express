import sqlite3
from item_model import ItemModel
from datetime_service import DateTimeService
from time_calculator import TimeCalculator


class SearchItemsAction:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path
        self.time_api = DateTimeService()
        self.time_calc = TimeCalculator()

    def execute(self, keyword="", category_filter=""):
        # 1. Preluăm ora curentă o singură dată per căutare de la API
        timp_curent = self.time_api.get_current_time()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = "SELECT id, title, category, location, date_time, status FROM items WHERE status = 'Activ'"
        params = []

        if keyword:
            query += " AND title LIKE ?"
            params.append(f"%{keyword}%")

        if category_filter:
            query += " AND category = ?"
            params.append(category_filter)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        results = []
        for row in rows:
            data_salvata = row[4]

            # 2. Calculăm diferența apelând noua clasă
            timp_trecut = self.time_calc.calcul_timp_trecut(data_salvata, timp_curent)

            # 3. Adăugăm rezultatul în model
            results.append(ItemModel(
                item_id=row[0], title=row[1], category=row[2],
                location=row[3], date_time=data_salvata, status=row[5],
                time_ago=timp_trecut
            ))

        return results