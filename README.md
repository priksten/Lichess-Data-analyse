# Lichess-Data-analyse

# Omschrijving:
Lichess.org is een online schaakserver waarop schakers van allerlei niveaus tegen elkaar kunnen schaken. Alle schaakpartijen die een bepaalde gebruiker op Lichess.org speelt, worden opgeslagen. Deze schaakpartijen kunnen op een moment naar keuze gedownload worden in een pgn-bestand. Een pgn-bestand is een tekstbestandsformaat waarin zowel de zetten van een schaakpartij als allerlei informatie over de partij (denk aan: namen van beide spelers, datum waarop de partij gespeeld is, het speeltempo, het resultaat van de partij, hoe lang een speler over elk van zijn zetten heeft nagedacht en de ratingen van beide spelers).  Er zijn verschilende schaakprogramma’s die gebruikt kunnen worden om pgn-bestanden te bekijken. 

Voorbeeld van hoe een pgn-bestand eruitziet:
![image](https://github.com/priksten/Lichess-Data-analyse/assets/85739742/aefde17b-ac1e-4b92-9bf8-763c84f9c78f)

Het doel van dit project was om in Python een programma te schrijven dat de schaker inzicht geeft in zijn prestaties. Hierbij gaat het om hoe de speler presteert:
•	Prestaties over de partijen: hoeveel winst, hoeveel remise, hoeveel verlies
•	Overzicht van het niveau van de tegenstanders
•	Het ratingverloop van de speler over deze partijen in een grafiek, waarbij ook de maximaal behaalde rating wordt aangegeven. 
•	De mogelijkheid bieden om de resultaten die met wit behaald zijn te vergelijken met de resultaten die met zwart behaald zijn

De manier waarop het programma werkt, is als volgt:
1.	De schaker downloadt zijn partijen van Lichess.org als een pgn-file
2.	Vervolgens laat deze schaker deze pgn-file omzetten naar een csv-bestand waarin alle partijgegevens overzichtelijk zijn weergegeven: elke rij staat voor de gegevens van één partij (via PGNtoCSV.py)
3.	Vervolgens kan de schaker dit CSV-bestand laten analyseren met behulp van Chess_Analysis_version4.py
4.	De output is een Excel-bestand met vier tabbladen waarin alle analyses staan (zie screenshots) 

# Programmeertaal + versie: 
Python

# Gebruikte modules:
- CSV
- Chesspy
- Math
- Matplotlib
- Numpy
- Pandas
- Pgn2data
- Pygal
- Xslxwriter

# Screenshots:
De uitvoer van de analyse is een Excel-bestand met daarin 4 tabbladen waarin de analyse te vinden is. 

Tabblad 1: Overzicht van de scores in het algemeen voor deze speler. Hierbij zijn de scores niet gesplitst op kleur
![image](https://github.com/priksten/Lichess-Data-analyse/assets/85739742/b1c2ca83-9a86-44c0-a416-7fbc2cc2a7aa)

Tabblad 2: De scores van de speler die hij heeft behaald wanneer hij met wit speelt
![image](https://github.com/priksten/Lichess-Data-analyse/assets/85739742/053bb012-e3ae-45f4-adff-6b19b18b4647)

Tabblad 3: De scores die de speler heeft behaald wanneer hij met zwart speelt
![image](https://github.com/priksten/Lichess-Data-analyse/assets/85739742/cbe78842-6e83-496d-9484-9ec49d843af8)

Tabblad 4: Het ratingverloop van de speler
![image](https://github.com/priksten/Lichess-Data-analyse/assets/85739742/794f2aa4-5cf8-4d67-8aa8-85ebdec42bca)

