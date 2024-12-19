# EPR_07_Team
Abgabe für die Teamaufgabe EPR_07

## 1. Analyse:
Das Programm wird objektorientiert entwickelt.

Zu den notwendigen Funktionalitäten gehören:
  1. Einlesen einer CSV-Datei, welche die angebotenen Produkte enthält. Diese Informationen sollendann innerhalb des Programms genutzt werden können.
  2. Bestellungen sollen pro Tisch vermerkt werden.
     - unter Einbeziehung von Nachbestellungen und Stornierungen
     - Sonderwünschen sollen berücksichtigt werden
       - wenn etwas hinzugewünscht wird soll sich der Preis um 1€ erhöhen
       - wenn etwas weggelassen wird bleibt der Preis unverändert
  3. Erstellen einer Rechnung für den Bezahlvorgang
     - Format der Rechnung soll eine TXT-Datei sein, welche die Bestellungen enthält und den Gesamtpreis

Die bereitgestellte CSV.Datei wird automatisch bei Programmstart eingelesen.
Die Bedienung erfolgt über die Konsole, worüber auch Hinweise zum Status der jeweils gewählten Vorgänge ausgegeben werden.
Eingaben müssen auf Korrektheit überprüft werden und fehlerhafte Eingaben dürfen nicht zum Absturz des Programms führen.
Zudem wird ein aussagekräftiges UI gewünscht und eine Funktion zum Beenden des Programms.

### Weitere Annahmen: 
Die Produkte unterscheiden sich eindeutig im Namen.
Abgesehen von den erstellten Rechnungen wird nicht gespeichert. Also keine Wiederaufnahme der Arbeit bei Neustart. (alle Werte bei Start auf Ausgangszustand)
 
### Zerlegung: 
Umsetzung als Klassen, deren Instanzen als Objekte in Listen gespeichert und darus aufgerufen, bzw. angesteuert werden können.
Jedes Modul enthält für die Übersicht eine einzelne Klasse, die können, wo notwendig, importiert werden.
Alles wird über eine main.py Datei funktional zusammengeführt und kann darüber gestartet werden.
 
### Ausgabe: 
Die Konsole, worüber das Programm gesteuert wird, gibt Hinweise zum Status der jeweils gewählten Vorgänge aus.
Die Ausgabe der Rechnungen erfolgt im Programmordner.

## Misc Infos:
- Der Gesamtpreis wird aus zwei Nachkommastellen gerundet.
- Keyword "extra" für +1€ bei Sonderwünschen, die etwas hinzufügen
- Der Inhalt der CSV-Datei muss das korrekte Format aufweisen
- Die im Lauf des Programms vergebenen IDs sind fortlaufend

- weiter Funktionen geplant, jedoch nicht bis zur Deadline final umsetzbar

## 2. Benutzerhandbuch

## 3. README
Das Programm „Order-Management-System“ stellt Funktionen für ein einfaches Verwaltungssystem bereit.
Es erlaubt für das Verwalten von Bestellungen pro Tisch in einem Restaurant und kann Rechnungen las TXT-Datei abspeichern

### Installation
Installiert sein muss ein Python-Interpreter 3.10 oder neuer mit den Bibliotheken und Support-Programmen der Standard-Installation von www.python.org .
Alle restlichen notwendigen Dateien sind im Ordner OMS enthalten, welcher auf die Datei zum Start des Programms enthält.

### Start des Programms
Man starte das Programm „Order-Management-System“ in der für das jeweilige Betriebssystem üblichen Art und Weise, aus der Interpreter-Shell oder in einer IDE, z.B. IDLE.
Weitere Angaben zur Dokumentation siehe 1. Analyse und bei Fragen zur Handhabung siehe 2. Benutzerhandbuch.

### bekannte Bugs:
Testfälle sind unter der enthaltenen Datei "testcases.pdf" zu finden.

#### food.csv
- Die Preise der CSV-Datei müssen als ein für Python zulässigen float eingetragen werden. Andernfalls sorgt eine falsche Hinterlegung des Preises zu Fehlern im Programm.
- Das passende Format innerhalb der CSV-Datei muss eingehalten werden (d.h. Name des Produkts in die erste Spalte und Preis in die vierte.)
