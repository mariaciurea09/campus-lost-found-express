class ItemModel:
    def __init__(self, title, category, location, date_time, status="Activ", item_id=None, time_ago=""):
        self.item_id = item_id
        self.title = title
        self.category = category
        self.location = location
        self.date_time = date_time
        self.status = status
        self.time_ago = time_ago  # Câmp pentru afișarea inteligentă