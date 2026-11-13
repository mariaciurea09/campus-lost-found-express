from datetime import datetime


class TimeCalculator:
    def calcul_timp_trecut(self, data_trecuta, data_curenta):
        """Primește două texte cu data/ora și returnează diferența în limbaj natural."""
        try:
            fmt = "%Y-%m-%d %H:%M:%S"
            past = datetime.strptime(data_trecuta, fmt)
            current = datetime.strptime(data_curenta, fmt)
            diff = current - past

            secunde = diff.total_seconds()

            if secunde < 60:
                return "acum câteva secunde"
            elif secunde < 3600:
                minute = int(secunde // 60)
                return f"acum {minute} minut{'e' if minute > 1 else ''}"
            elif secunde < 86400:
                ore = int(secunde // 3600)
                return f"acum {ore} or{'ă' if ore == 1 else 'e'}"
            elif secunde < 2592000:
                zile = int(secunde // 86400)
                return f"acum {zile} zi{'le' if zile > 1 else ''}"
            else:
                luni = int(secunde // 2592000)
                return f"acum {luni} lun{'ă' if luni == 1 else 'i'}"
        except ValueError:
            return "dată nerecunoscută"