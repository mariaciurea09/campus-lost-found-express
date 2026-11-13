from db_init import DatabaseInitializer
from add_item_action import AddItemAction
from search_items_action import SearchItemsAction
from update_status_action import UpdateStatusAction
from alert_manager_action import AlertManagerAction


class CampusLostFoundController:
    def __init__(self, db_path="campus_lf.db"):
        self.db_path = db_path

        # Instanțierea claselor de acțiune
        self.db_init = DatabaseInitializer(self.db_path)
        self.add_action = AddItemAction(self.db_path)
        self.search_action = SearchItemsAction(self.db_path)
        self.update_action = UpdateStatusAction(self.db_path)
        self.alert_action = AlertManagerAction(self.db_path)

    def initialize_system(self):
        """Inițializează tabelele bazei de date."""
        return self.db_init.execute()

    def add_item(self, title, category, location):
        """Adaugă un obiect nou folosind timpul generat automat și verifică alerte."""
        new_id = self.add_action.execute(title, category, location)
        alerts_triggered = self.alert_action.execute(title, category)

        return {"new_id": new_id, "alerts": alerts_triggered}

    def search_active_items(self, keyword="", category_filter=""):
        """Caută obiectele active și marchează timpul acțiunii."""
        return self.search_action.execute(keyword, category_filter)

    def mark_as_recovered(self, item_id):
        """Schimbă starea unui obiect în 'Recuperat'."""
        return self.update_action.execute(item_id, "Recuperat")