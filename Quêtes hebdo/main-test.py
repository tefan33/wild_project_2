# Importe la classe FastAPI depuis le module fastapi
from fastapi import FastAPI

# Création d'un dictionnaire qui va être interrogé par une API
items = {
    "234566": "100$",    # ID: Prix
    "234567": "130$",
    "234568": "120$",
    "234569": "400$",
    "234570": "300$",
    "234571": "130$"
}

# Crée une instance de l'application FastAPI
app = FastAPI()

# Définis une route pour l'URL "/"
# Lorsqu'un client accède à cette URL avec une méthode GET, la fonction "root" sera appelée


@app.get("/")
def root():
    
    """
    Renvoie un message "Hello World".
    
    """
    
    # Le contenu de cette fonction sera renvoyé comme réponse à la requête
    return {"message": "Hello World"}

@app.get("/items")
def get_items():
    """
    Retourne la liste des ID des items avec leur prix.
    """
    return items


@app.get("/items/{id}")
def get_items(id):
    """
    Récupère le prix d'un article en fonction de son ID.
    """
    # Vérifie si l'ID de l'article existe dans le dictionnaire des articles
    if id in items:
        # Retourne le prix de l'article correspondant à l'ID
        return items[id]
    else:
        # Retourne une réponse indiquant que l'article n'a pas été trouvé
        return "Article non trouvé"
    
@app.get("/id/{id}")
def read_id(id: int) -> dict:
    return {"read_id": id}


