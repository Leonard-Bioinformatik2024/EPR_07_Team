# EPR_07_Team
Abgabe für die Teamaufgabe EPR_07

Das Programm „Order-Management-System“ stellt Funktionen bereit, die es ermöglichen Bestellungen pro Tisch entgegen zu nehmen und Rechnungen zu Erstellen.

Installiert sein muss ein Python-Interpreter 3.10 oder neuer mit den Bibliotheken und Support-
Programmen der Standard-Installation von www.python.org .

Man startet das Programm „Order-Management-System“ über die Datei "main.py" aus dem Ordner "OMS" in der für das jeweilige Betriebssystem üblichen Art
und Weise, aus der Interpreter-Shell oder in einer IDE, z.B. IDLE.

## Misc Infos:
- Der Gesamtpreis wird aus zwei Nachkommastellen gerundet.
- Keyword "extra" für +1€ bei Sonderwünschen, die etwas hinzufügen

## bekannte Bugs:
### food.csv
- Die Preise der CSV-Datei müssen als ein für Python zulässigen float eingetragen werden. Andernfalls sorgt eine falsche Hinterlegung des Preises zu Fehlern im Programm.
- Das passende Format innerhalb der CSV-Datei muss eingehalten werden (d.h. Name des Produkts in die erste Spalte und Preis in die vierte.)
