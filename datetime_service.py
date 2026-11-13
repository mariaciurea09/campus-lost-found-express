import requests
from datetime import datetime


class DateTimeService:
    def __init__(self):
        self.api_url = "https://time.now/developer/api/time?timezone=Europe%2FBucharest"

    def get_current_time(self):
        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            data = response.json()

            raw_time = data.get('datetime') or data.get('time') or str(data)

            # Păstrăm doar YYYY-MM-DD HH:MM:SS (fără fus orar și litera T)
            if "T" in raw_time:
                return raw_time[:19].replace("T", " ")
            return raw_time

        except requests.RequestException:
            # Dacă API-ul pică, luăm ora locală a calculatorului ca variantă de rezervă
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")