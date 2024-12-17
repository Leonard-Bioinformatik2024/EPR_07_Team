"""This module contains the class Rechnung.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from datetime import datetime

class Rechnung:
    def __init__(self, tisch):
        self.tisch = tisch
        self.datum = datetime.now()
        self.gesamtpreis = self.tisch.berechne_gesamtpreis()

    def erstelle_rechnung(self):
        """Speichert die Rechnung als .txt-Datei."""
        dateiname = f"rechnung_tisch_{self.tisch.nummer}_{self.datum.strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(dateiname, "w", encoding="utf-8") as file:
                file.write(f"Rechnung für Tisch {self.tisch.nummer}\n")
                file.write(f"Datum: {self.datum.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                file.write("Bestellungen:\n")
                for bestellung in self.tisch.bestellungen:
                    file.write(f"  {bestellung}\n")
                file.write(f"\nGesamtpreis: {self.gesamtpreis:.2f} EUR\n")
            print(f"Rechnung wurde unter {dateiname} gespeichert.")
        except Exception as e:
            print(f"Fehler beim Speichern der Rechnung: {e}")
