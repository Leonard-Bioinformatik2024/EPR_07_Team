"""This module contains the class Restaurant.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


import pandas as pd
from tisch import Tisch
from produkt import Produkt


class Restaurant:
    def __init__(self):
        self.tische = []
        self.produkte = []

    def lade_produkte(self):
        """Lädt Produkte aus einer CSV-Datei."""
        try:
            with open('food.csv', mode='r', encoding='utf-8') as csvfile:
                df = pd.read_csv(csvfile, sep=';')
                for row in range(len(df)):
                    produkt = Produkt(name=df.values[row][0], price=float(df.values[row][3]))
                    self.produkte.append(produkt)
            print("Produkte erfolgreich geladen.")
        except FileNotFoundError:
            print("Datei nicht gefunden. Bitte überprüfen Sie den Pfad.")
        except KeyError:
            print("Fehlerhafte CSV-Datei. \
                  Stellen Sie sicher, dass die Spalten 'name' und 'price' vorhanden sind.")

    def finde_tisch(self, tischnummer):
        """Findet einen Tisch anhand seiner Nummer."""
        for tisch in self.tische:
            if tisch.nummer == tischnummer:
                return tisch
        return None

    def finde_produkt(self, produktname):
        """Findet ein Produkt anhand seines Namens."""
        for produkt in self.produkte:
            if produkt.name.lower() == produktname.lower():
                return produkt
        return None

    def hinzufuegen_tisch(self, tischnummer):
        """Fügt einen neuen Tisch hinzu."""
        if self.finde_tisch(tischnummer):
            print(f"Tisch {tischnummer} existiert bereits.")
        else:
            neuer_tisch = Tisch(tischnummer)
            self.tische.append(neuer_tisch)

if __name__ == "__main__":
    Restaurant.lade_produkte('x')
