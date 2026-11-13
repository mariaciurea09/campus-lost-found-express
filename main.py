from app_controller import CampusLostFoundController


def meniu_principal():
    app = CampusLostFoundController()
    app.initialize_system()

    while True:
        print("\n" + "=" * 45)
        print("   CAMPUS LOST & FOUND EXPRESS - MENIU")
        print("=" * 45)
        print("1. Adaugă un obiect găsit")
        print("2. Caută obiecte active (sau afișează-le pe toate)")
        print("3. Marchează un obiect ca „Recuperat”")
        print("4. Ieșire")

        optiune = input("\nAlege o opțiune (1-4): ").strip()

        if optiune == "1":
            print("\n--- Adăugare obiect nou ---")
            titlu = input("Titlu obiect (ex. Chei, Portofel): ")
            categorie = input("Categorie (ex. Electronice, Accesorii, Acte): ")
            locatie = input("Locație preluare (ex. Sala A101, Cantină): ")

            try:
                rezultat = app.add_item(titlu, categorie, locatie)
                print(f"[SUCCES] Obiectul a fost salvat cu ID-ul: {rezultat['new_id']}")
                if rezultat["alerts"]:
                    print(f"[ALERTĂ] Notificări trimise către: {', '.join(rezultat['alerts'])}")
            except ValueError as e:
                print(f"[EROARE VALIDARE] {e}")
            except Exception as e:
                print(f"[EROARE] {e}")

        elif optiune == "2":
            print("\n--- Căutare obiecte active ---")
            cuvant = input("Cuvânt-cheie (apasă Enter pentru toate): ").strip()
            categorie = input("Filtru categorie (apasă Enter pentru toate): ").strip()

            rezultate = app.search_active_items(keyword=cuvant, category_filter=categorie)
            if not rezultate:
                print("Nu s-au găsit obiecte active care să corespundă căutării.")
            else:
                print(f"\nS-au găsit {len(rezultate)} obiect(e) active:")

                # Aici folosim noul câmp time_ago calculat curat de backend
                for obj in rezultate:
                    print(f"  ID: {obj.item_id} | {obj.title} [{obj.category}] - Locație: {obj.location}")
                    print(f"      -> Adăugat {obj.time_ago} (Data exactă: {obj.date_time})")

        elif optiune == "3":
            print("\n--- Marcare obiect ca Recuperat ---")
            id_text = input("Introdu ID-ul obiectului recuperat: ").strip()

            if not id_text.isdigit():
                print("[EROARE] ID-ul trebuie să fie un număr întreg (ex. 3).")
                continue

            try:
                mesaj = app.mark_as_recovered(int(id_text))
                print(f"[SUCCES] {mesaj}")
            except ValueError as e:
                print(f"[EROARE] {e}")

        elif optiune == "4":
            print("Ieșire din aplicație.")
            break
        else:
            print("[EROARE] Opțiune invalidă. Alege un număr între 1 și 4.")


if __name__ == "__main__":
    meniu_principal()