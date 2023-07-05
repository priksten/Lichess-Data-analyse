import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import pygal
import pandas as pd
#import openpyxl
import xlsxwriter


filename = 'lichess_Rikstov88_2023-06-28 (3)_game_info.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)


    # We maken lijsten aan waarin de gegevens uit het dataframe worden opgenomen, zodat deze daarna geanalyseerd kunnen worden
    datum_partij = []
    nummer_partij = []
    speler_wit = []
    speler_zwart = []
    rating_wit = []
    rating_zwart = []
    winnaar = []
    verliezer = []

    # Hier vullen we de lijsten met de gegevens uit de relevante kolommen van het dataframe
    for row in reader:
        datum_partij.append(row[4])
        nummer_partij.append(row[1])
        speler_wit.append(row[6])
        speler_zwart.append(row[7])
        rating_wit.append(row[9])
        rating_zwart.append(row[11])
        winnaar.append(row[15])
        verliezer.append(row[17])
    
# De partijen staan in omgekeerde chronologische volgorde, dus we moeten de volgorden in bovenstaande lijsten omdraaien.
datum_partij.reverse()
speler_wit.reverse()
speler_zwart.reverse()
rating_wit.reverse()
rating_zwart.reverse()
winnaar.reverse()
verliezer.reverse()

# Algemene analyse. Hierin de volgende gegevens:
#   - aantal partijen gespeeld
#   - aantal wit
#   - aantal zwart
#   - aantal partijen winst
#   - aantal partijen remise
#   - aantal partijen verlies
# Hierbij ook procentuele scores

aantal_totaal = len(datum_partij)
aantal_winst = 0
aantal_remise = 0
aantal_verlies = 0

for speler in winnaar:
    if speler == 'Rikstov88':
        aantal_winst += 1
    elif speler == 'draw':
        aantal_remise += 1

for speler in verliezer:
    if speler == 'Rikstov88':
        aantal_verlies += 1

winst_perc = round(100 * aantal_winst/aantal_totaal, 0)
remise_perc = round (100* aantal_remise/aantal_totaal, 0)
verlies_perc = round(100*aantal_verlies/aantal_totaal, 0)

prestaties_algemeen_abs = [aantal_winst, aantal_remise, aantal_verlies, aantal_totaal]
prestaties_algemeen_rel = [winst_perc, remise_perc, verlies_perc, '100']
prestaties_index = ['Winst', 'Remise', 'Verlies', 'Totaal']

prestaties_algemeen = {
    "Aantal" : prestaties_algemeen_abs,
    "Procent van totaal" : prestaties_algemeen_rel
}

df_prestaties_algemeen = pd.DataFrame(prestaties_algemeen, prestaties_index)

# Hier berekenen we de prestaties per kleur:
#   - aantal partijen gespeeld
#   - aantal wit
#   - aantal zwart
#   - aantal partijen winst
#   - aantal partijen remise
#   - aantal partijen verlies
# Hierbij ook procentuele scores
aantal_wit = 0
winst_wit = 0
remise_wit = 0
verlies_wit = 0

aantal_zwart = 0
winst_zwart = 0
remise_zwart = 0
verlies_zwart = 0

for speler in speler_wit:
    if speler == 'Rikstov88':
        aantal_wit += 1

for index in range(0, aantal_totaal) :
    if speler_wit[index] == 'Rikstov88' and winnaar[index] == 'Rikstov88':
        winst_wit += 1
    elif speler_wit[index] == 'Rikstov88' and winnaar[index] == 'draw':
        remise_wit += 1
    elif speler_wit[index] == 'Rikstov88' and verliezer[index] == 'Rikstov88':
        verlies_wit += 1 

wit_winst_perc = round(100 * winst_wit/aantal_wit, 0)
wit_remise_perc = round (100* remise_wit/aantal_wit, 0)
wit_verlies_perc = round(100* verlies_wit/aantal_wit, 0)

prestaties_wit_abs = [winst_wit, remise_wit, verlies_wit, aantal_wit]
prestaties_wit_rel = [wit_winst_perc, wit_remise_perc, wit_verlies_perc, '100']

prestaties_wit = {
    "Aantal": prestaties_wit_abs,
    "Procent van totaal": prestaties_wit_rel
}

df_prestaties_wit = pd.DataFrame(prestaties_wit, prestaties_index)

rating_opp_zwart = []

for index in range(0, aantal_totaal):
    if speler_wit[index] == 'Rikstov88':
        rating = rating_zwart[index]
        rating_opp_zwart.append(rating)

for index in range(len(rating_opp_zwart)):
    rating_opp_zwart[index] = int(rating_opp_zwart[index])

hoogste_zwart_opp = round(max(rating_opp_zwart), 0)
laagste_zwart_opp = round(min(rating_opp_zwart), 0) 
gem_zwart_opp = round(np.mean(rating_opp_zwart), 0)
std_zwart_opp = round(np.std(rating_opp_zwart), 0)

zwart_tegenstanders_rating = [gem_zwart_opp, std_zwart_opp, laagste_zwart_opp, hoogste_zwart_opp]
index_tegenstanders_rating = ['Gemiddelde', 'Standaardafwijking', 'Minimum', 'Maximum'] 

zwart_tegenstanders = {
    "Rating tegenstander": zwart_tegenstanders_rating
}

df_zwart_tegenstanders = pd.DataFrame(zwart_tegenstanders, index_tegenstanders_rating)

for speler in speler_zwart:
    if speler == 'Rikstov88':
        aantal_zwart += 1

for index in range(0, aantal_totaal):
    if speler_zwart[index] == 'Rikstov88' and winnaar[index] == 'Rikstov88':
        winst_zwart += 1
    elif speler_zwart[index] == 'Rikstov88' and winnaar[index] == 'draw':
        remise_zwart += 1
    elif speler_zwart[index] == 'Rikstov88' and verliezer[index] == 'Rikstov88':
        verlies_zwart += 1 

zwart_winst_perc = round(100 * winst_zwart/aantal_zwart, 0)
zwart_remise_perc = round (100* remise_zwart/aantal_zwart, 0)
zwart_verlies_perc = round(100* verlies_zwart/aantal_zwart, 0)

prestaties_zwart_abs = [winst_zwart, remise_zwart, verlies_zwart, aantal_zwart]
prestaties_zwart_rel = [zwart_winst_perc, zwart_remise_perc, zwart_verlies_perc, '100']

prestaties_zwart = {
    "Aantal": prestaties_zwart_abs,
    "Procent van totaal": prestaties_zwart_rel
}

df_prestaties_zwart = pd.DataFrame(prestaties_zwart, prestaties_index)

rating_opp_wit = []

for index in range(0, aantal_totaal):
    if speler_zwart[index] == 'Rikstov88':
        rating = rating_wit[index]
        rating_opp_wit.append(rating)

for index in range(len(rating_opp_wit)):
    rating_opp_wit[index] = int(rating_opp_wit[index])

hoogste_wit_opp = round(max(rating_opp_wit),0)
laagste_wit_opp = round(min(rating_opp_wit),0) 
gem_wit_opp = round(np.mean(rating_opp_wit),0)
std_wit_opp = round(np.std(rating_opp_wit), 0)

wit_tegenstanders_rating = [gem_wit_opp, std_wit_opp, laagste_wit_opp, hoogste_wit_opp]
index_tegenstanders_rating = ['Gemiddelde', 'Standaardafwijking', 'Minimum', 'Maximum'] 

wit_tegenstanders = {
    "Rating tegenstander": wit_tegenstanders_rating
}

df_wit_tegenstanders = pd.DataFrame(wit_tegenstanders, index_tegenstanders_rating)

# Analyse van ratings. Hiervoor hebben we als eerste twee nieuwe lijsten nodig:
# - Lijst 1: lijst van eigen rating per partijnummer (rating_lijst)
# - Lijst 2: lijst van tegenstanders-rating per partijnummer (tegenstander_rating_lijst)
# We gaan door zowel speler_wit en speler_zwart. We checken op de conditie of de naam in de lijst 'Rikstov 88' is. 
# Als dit zo is, gebruiken we deze index om de bijbehorende rating uit de lijsten rating_wit en rating_zwart te halen. 

rating_lijst = []
tegenstander_rating_lijst = []

for i in range(aantal_totaal):
    if speler_wit[i] == 'Rikstov88':
        rating = rating_wit[i]
    
    elif speler_zwart[i] == 'Rikstov88':
        rating = rating_zwart[i]
            
    rating_lijst.append(rating)

for i in range(aantal_totaal):
    if speler_wit[i] != 'Rikstov88':
        rating_opp = rating_wit[i]
    elif speler_zwart[i] != 'Rikstov88':
        rating_opp = rating_zwart[i]

    tegenstander_rating_lijst.append(rating_opp)
    
# We willen de volgende dingen gaan produceren op basis van de lijst eigen rating:
#   - grafiek rating verloop
#   - hoogste eigen rating
#   - laagste eigen rating
#   - gemiddelde eigen rating
# Merk op dat rating_lijst een lijst met strings is, dus eerst moeten we alle strings omzetten in integers

for index in range(aantal_totaal):
    rating_lijst[index] = int(rating_lijst[index])

gem_rating = round(np.mean(rating_lijst), 0)
std_rating = round(np.std(rating_lijst), 0)
max_rating = round(max(rating_lijst),0)
min_rating = round(min(rating_lijst), 0)

rating_overzicht = [gem_rating, std_rating, min_rating, max_rating]
behaalde_rating = {
    "Behaalde rating": rating_overzicht
}

df_behaalde_rating = pd.DataFrame(behaalde_rating, index_tegenstanders_rating)

# Plot maken voor behaalde rating
partijnummer = list(range(1, aantal_totaal+1))
plt.plot(partijnummer, rating_lijst, linewidth = 5)

plt.title("Rating Rikstov88")
plt.xlabel("Partijnummer", fontsize = 14)
plt.ylabel("Rating", fontsize = 14)
plt.savefig('rating.png')

plt.show()

# We willen de volgende dingen gaan produceren op basis van de lijst rating tegenstanders:
#   - hoogste rating tegenstander
#   - laagste rating tegenstander
#   - gemiddelde rating tegenstander
# Merk op dat rating_lijst een lijst met strings is, dus eerst moeten we alle strings omzetten in integers

for index in range(aantal_totaal):
    tegenstander_rating_lijst[index] = int(tegenstander_rating_lijst[index])

gem_opp_rating = round(np.mean(tegenstander_rating_lijst), 0)
std_opp_rating = round(np.std(tegenstander_rating_lijst), 0)
max_opp_rating = round(max(tegenstander_rating_lijst), 0)
min_opp_rating = round(min(tegenstander_rating_lijst), 0)

algemeen_tegenstanders_rating = [gem_opp_rating, std_opp_rating, min_opp_rating, max_opp_rating]
index_tegenstanders_rating = ['Gemiddelde', 'Standaardafwijking', 'Minimum', 'Maximum'] 

algemeen_tegenstanders = {
    "Rating tegenstander": algemeen_tegenstanders_rating
}

df_algemeen_tegenstanders_rating = pd.DataFrame(algemeen_tegenstanders, index_tegenstanders_rating)

# Staafdiagram met daarin behaalde score tegen tegenstanders in een bepaalde ratingklasse
# Methode: 
# - eerst bepalen we de ondergrens van de laagste ratingklasse en de bovengrens van de hoogste ratingklasse (beiden afgerond naar hele honderdtal resp. onder en boven de grens).
# - ten tweede maken we een lijst 'grenzen' die in stappen van 50 of 100 van laagste hondertal naar hoogste honderdtal gaat 
# - ten derde laten we Python voor elke i in 'grenzen' tellen hoeveel ratings er tussen grenzen[i] en grenzen [i+1] zitten. 
#       (dit geeft de lijst 'frequenties')
# - ten vierde, maken we een staafdiagram met op de x-as de lijst 'grenzen' en op de y-as de lijst 'frequenties'

ondergrens = math.floor(min_opp_rating/100)*100
bovengrens = math.ceil(max_opp_rating/100)*100

grenzen = list(range(ondergrens, bovengrens + 100, 100))

counter = 0
count_score = 0
frequenties = []
x_labels = []
scores = []

for i in range(0, len(grenzen)-1):
    for j in range(len(tegenstander_rating_lijst)):
        if tegenstander_rating_lijst[j] >= grenzen[i] and tegenstander_rating_lijst[j] < grenzen[i+1]:
            counter += 1
            if winnaar[j] == 'Rikstov88':
                count_score += 1
            elif winnaar[j] == 'draw':
                count_score += 0.5
    frequenties.append(counter)
    scores.append(count_score)
    counter = 0
    count_score = 0
    x_labels.append(str(grenzen[i]) + ' - ' + str(grenzen[i+1]))

proc_scores = []

for index in range(0, len(grenzen)-1):
    proc_score = round(100* scores[index]/frequenties[index],0)
    proc_scores.append(proc_score)
    proc_score = 0

frequentietabel_tegenstanders = {
    "Ratingklasse": x_labels,
    "Aantal partijen": frequenties,
    "Score": scores,
    "Procentuele score": proc_scores
}

df_frequentietabel = pd.DataFrame(frequentietabel_tegenstanders)

hist_opp_rating = pygal.Bar()
hist_opp_rating.title = "Overzicht tegenstanders"
hist_opp_rating.x_labels = x_labels
hist_opp_rating.x_title = "Ratingklasse"
hist_opp_rating.y_title = "Score in procenten"

hist_opp_rating.add('Score in procenten', proc_scores)
hist_opp_rating.render_to_file('proc_rating_opp_visual.svg')

# We printen nu alle dataframes in een logische volgorde:
#   1. alle dataframes die betrekking hebben op algemeen
#   2. alle dataframes die betrekking hebben op mijn prestaties met wit
#   3. alle dataframes die betrekking hebben op mijn prestaties met zwart
#   4. het dataframe + de plot van mijjn behaalde ratings

print('Algemene prestaties: ')
print(df_prestaties_algemeen)
print(' ')

print('Tegenstanders info algemeen:')
print(df_algemeen_tegenstanders_rating)
print(' ')

print('Frequentieverdeling tegenstanders:')
print(df_frequentietabel)
print('----------------------------------------------------------- ')
print(' ')

print('Prestaties met wit:')
print(df_prestaties_wit)
print(' ')

print('Wit - Rating Info Tegenstanders (tegenstander heeft dus zwart): ')
print(df_zwart_tegenstanders)
print('----------------------------------------------------------- ')
print(' ')

print('Prestaties met zwart:')
print(df_prestaties_zwart)
print(' ')

print('Zwart - Rating Info Tegenstanders (tegenstander heeft dus wit): ')
print(df_wit_tegenstanders)
print('----------------------------------------------------------- ')
print(' ')

print('Overzicht behaalde rating in deze dataset: ')
print(df_behaalde_rating)


# Nu willen we al deze dataframes in een excel- of csv-bestand inlezen
#
writer = pd.ExcelWriter('OutputAnalysis.xlsx', engine='xlsxwriter')
df_prestaties_algemeen.to_excel(writer, sheet_name='Algemeen') 
df_algemeen_tegenstanders_rating.to_excel(writer, sheet_name='Algemeen', startrow= 7 )
df_frequentietabel.to_excel(writer, sheet_name='Algemeen', startrow=15) 
df_prestaties_wit.to_excel(writer,sheet_name='Prestaties_Wit') 
df_zwart_tegenstanders.to_excel(writer, sheet_name='Prestaties_Wit', startrow= 7)
df_prestaties_zwart.to_excel(writer,sheet_name='Prestaties_Zwart')
df_wit_tegenstanders.to_excel(writer, sheet_name='Prestaties_Zwart', startrow= 7)
df_behaalde_rating.to_excel(writer,sheet_name='Rating_overzicht') 

worksheet = writer.sheets['Rating_overzicht']
worksheet.insert_image('F1', 'rating.png')

writer._save()