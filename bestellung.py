"""This module contains the class Bestellung.
"""


__author__ = "8532653, Hoffmann"
__email__ = "leonard.hoffmann@stud.uni-frankfurt.de"


from produkt import Produkt

class Bestellung:
    id_counter = 1

    def __init__(self, produkt, sonderwuensche=None):
        if not isinstance(produkt, Produkt):
            raise ValueError("Ungültiges Produkt übergeben.")

        self.id = Bestellung.id_counter
        Bestellung.id_counter += 1

        self.produkt = produkt
        self.sonderwuensche = sonderwuensche if sonderwuensche else []

    def berechne_preis(self):
        """Berechnet den Preis der Bestellung einschließlich Sonderwünsche."""
        zusatzkosten = sum(1 for wunsch in self.sonderwuensche if "extra" in wunsch.lower())
        return self.produkt.price + zusatzkosten

    def __str__(self):
        sonderwuensche_text = ", ".join(self.sonderwuensche) if self.sonderwuensche else "Keine"
        return f"Bestellung ID: {self.id}, Produkt: {self.produkt.name}, \
            Preis: {self.berechne_preis()} EUR, Sonderwünsche: {sonderwuensche_text}"
