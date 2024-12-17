"""This is an order and billing system for a restaurant.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from restaurant import Restaurant
from bestellung import Bestellung
from rechnung import Rechnung

def main():
    print("Willkommen zum Restaurant-Management-System!")

    # Restaurant initialisieren
    restaurant = Restaurant()

    # Produkte aus CSV-Datei laden
    restaurant.lade_produkte()

    while True:
        print("\nHauptmenü")
        print("1. Neuer Tisch")
        print("2. Bestellung aufnehmen")
        print("3. Rechnung erstellen")
        print("4. Programm beenden")

        auswahl = input("Wählen Sie eine Option: ")

        if auswahl == "1":
            tischnummer = int(input("Geben Sie die Tischnummer ein: "))
            restaurant.hinzufuegen_tisch(tischnummer)
            print(f"Tisch {tischnummer} wurde hinzugefügt.")

        elif auswahl == "2":
            tischnummer = int(input("Geben Sie die Tischnummer ein: "))
            tisch = restaurant.finde_tisch(tischnummer)
            if not tisch:
                print("Tisch nicht gefunden.")
                continue

            produktname = input("Geben Sie den Namen des Produkts ein: ")
            produkt = restaurant.finde_produkt(produktname)
            if not produkt:
                print("Produkt nicht gefunden.")
                continue

            sonderwuensche = input("Geben Sie Sonderwünsche ein \
                                   (Komma getrennt, leer lassen für keine): ").split(",")
            sonderwuensche = [sw.strip() for sw in sonderwuensche if sw.strip()]

            bestellung = Bestellung(produkt, sonderwuensche)
            tisch.hinzufuegen_bestellung(bestellung)
            print("Bestellung wurde aufgenommen.")

        elif auswahl == "3":
            tischnummer = int(input("Geben Sie die Tischnummer ein: "))
            tisch = restaurant.finde_tisch(tischnummer)
            if not tisch:
                print("Tisch nicht gefunden.")
                continue

            rechnung = Rechnung(tisch)
            rechnung.erstelle_rechnung()
            print(f"Rechnung für Tisch {tischnummer} wurde erstellt und gespeichert.")

        elif auswahl == "4":
            print("Programm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
