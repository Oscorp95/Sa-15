import pandas as pd
import csv
import matplotlib.pyplot as plt
def OpenFile(name_csv, name_html):
    file = pd.read_csv(name_csv, delimiter=';')
    html_string = file.to_html()
    htmlfile = open(name_html, 'w')
    htmlSetup = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>SAE15-Traiter des donnees</title>
    </head>
    <body>
        <h1>Liste des soldats marocains morts pour la France pendant la Premiere Guerre Mondiale</h1>
        <br>
        <p>Explication sur le choix de ce jeu de donnees :</p>
        <p>
            Lors de ma recherche d'un jeu de donnees pour cette etude, j'ai choisi de me pencher sur la "Liste des soldats marocains morts pour la France pendant la Premiere Guerre Mondiale".
        </p>
        <p>
            Ce choix a ete motive par le desir de rendre hommage et de retracer l'histoire souvent meconnue de ces soldats marocains qui ont sacrifie leur vie pour la France durant ce conflit majeur. A travers cette analyse, je souhaite mettre en lumiere leur contribution et leur devouement, honorant ainsi leur memoire et soulignant l'importance de reconnaitre les sacrifices de ceux qui ont combattu pour la paix.
        </p>
        <br>
        {}
    </body>
    </html>
    """.format(html_string)
    htmlfile.write(htmlSetup)



def generate_histogram(dates):
    valid_dates = pd.to_datetime(dates, dayfirst=True).dropna()
    plt.hist(valid_dates, bins=20, edgecolor='k', alpha=0.7)
    plt.xticks(rotation=45)
    plt.xlabel('Date de décès')
    plt.ylabel('Nombre de décès')
    plt.title('Histogramme des dates de décès')
    plt.tight_layout()
    plt.savefig('histogramme_dates_deces.png')
    plt.show()



def run():
    indexHTML = open('index.html', 'w')
    indexText = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>SAE15-Traiter des donnees</title>
    </head>
    <body>
        <header class="header">
            <h1 id="name">Sae 15 by Merwan Ali benyahya</h1>
            <a href="./assets/file.zip">Telecharger le projet avec le jeu de donnees choisie et le fichiers</a>
            <a href="array.html">voir le tableau</a>
        </header>
        <div class="container">
            <img src="histogramme_dates_deces.png" alt="graph de deces">
        </div>
    </body>
    </html>
    """
    indexHTML.write(indexText)
    OpenFile('Soldat.csv', 'array.html')
    file = pd.read_csv('Soldat.csv', delimiter=";")
    dates = file["Date deces"]
    generate_histogram(dates)

run()