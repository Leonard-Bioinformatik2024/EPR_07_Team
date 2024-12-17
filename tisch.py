"""This module contains the class Tisch.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from bestellung import Bestellung

class Tisch:
    def __init__(self, nummer):
        self.nummer = nummer
        self.bestellungen = []

    def hinzufuegen_bestellung(self, bestellung):
        """Fügt eine neue Bestellung hinzu."""
        if isinstance(bestellung, Bestellung):
            self.bestellungen.append(bestellung)
            print(f"Bestellung wurde zu Tisch {self.nummer} hinzugefügt.")
        else:
            print("Ungültige Bestellung. Es wurde kein Objekt vom Typ 'Bestellung' übergeben.")

    def entferne_bestellung(self, bestell_id):
        """Entfernt eine Bestellung anhand ihrer ID."""
        for bestellung in self.bestellungen:
            if bestellung.id == bestell_id:
                self.bestellungen.remove(bestellung)
                print(f"Bestellung mit ID {bestell_id} wurde von Tisch {self.nummer} entfernt.")
                return
        print(f"Keine Bestellung mit ID {bestell_id} bei Tisch {self.nummer} gefunden.")

    def berechne_gesamtpreis(self):
        """Berechnet den Gesamtpreis aller Bestellungen an diesem Tisch."""
        gesamtpreis = sum(bestellung.berechne_preis() for bestellung in self.bestellungen)
        return gesamtpreis

    def zeige_bestellungen(self):
        """Zeigt alle Bestellungen an diesem Tisch an."""
        if not self.bestellungen:
            print(f"Keine Bestellungen für Tisch {self.nummer}.")
            return

        print(f"Bestellungen für Tisch {self.nummer}:")
        for bestellung in self.bestellungen:
            print(f"  ID: {bestellung.id}, Produkt: {bestellung.produkt.name}, Preis: {bestellung.berechne_preis()} EUR")
