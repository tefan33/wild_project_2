# Importe la classe FastAPI depuis le module fastapi
from fastapi import FastAPI
import pandas as pd


# lien des données à récupérer et création du dataframe
link = "communes_france.csv"
data = pd.read_csv(link)

# on retire la colonne unnamed qui est un index
data.drop(['Unnamed: 0'], axis=1, inplace=True)

# création d'un dictionnaire du nombre de villes par région 
dico_region = data["nom_commune_complet"].groupby(data["nom_region"]).agg(["count"]).to_dict()['count']

# Crée une instance de l'application FastAPI
app = FastAPI()

# Définis une route pour l'URL "/"
# Lorsqu'un client accède à cette URL avec une méthode GET, la fonction "root" sera appelée


@app.get("/")
def root():
    
    """
    Renvoie un message d'explication.
    
    """
    
    # Le contenu de cette fonction sera renvoyé comme réponse à la requête
    return {"Informations": "Vous devez naviguer dans les différentes parties de cette API pour avoir vos résultats. ville, region, departement et insee"}


# création de la partie ville avec l'utilisation du dictionnaire des région créé précédemment
@app.get("/ville/")
def get_ville():
    """
    Retourne le nombre de villes par région.
    """
    return dico_region

# création d'une partie région avec la liste des départements par région. 
@app.get("/region/{region}")
def get_region(region):
    """
    Retourne les départements d'une région avec leur nombre de communes..
    """
    #on test si la région existe
    if region in list(data["nom_region"]):
        # si ok on va crééer la recherche pour l'afficher. On regroupe les départements pour les compter par région
        return data[data["nom_region"] == region].groupby(["nom_departement"]).size().reset_index(name='counts').set_index('nom_departement').to_dict()['counts']
    else:
        # si nok on indique le problème
        return ("Cette région n'existe pas !!")

# création d'une partie departement avec la liste des commune avec leur code insee 
@app.get("/departement/{departement}")
def get_departement(departement):
    """
    Retourne les communes d'un département avec leur code commune INSEE.
    """
    # si ok on va crééer la recherche pour l'afficher. On regroupe les communes avec leur code insee regroupées par departement
    if departement in list(data["nom_departement"]):
        return data[data["nom_departement"] == departement][['nom_commune_complet','code_commune_INSEE']].set_index('nom_commune_complet').to_dict()['code_commune_INSEE']
    else:
        # si nok on indique le problème
        return ("Ce département n'existe pas !!")
    
# création d'une partie code avec la liste des informations par le code insee 
@app.get("/insee/{code}")
def get_code(code):
    """
    Retourne les informations d'un code Insee (code_commune_INSEE, code_postal, latitude, longitude, nom_commune_complet, nom_département et nom_region ).
    """
    # si ok on retourne la liste
    if code in list(data['code_commune_INSEE']):
        return data[data["code_commune_INSEE"] == str(code)].to_dict('records')[0]
    else:
        # si nok on indique le problème
        return ("Ce code INSEE n'existe pas !!")
