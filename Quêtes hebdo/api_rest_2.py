from flask import Flask
from flask_restful import Resource, Api
import datetime as dt

# lecture du fichier csv en ligne pour l'analyser

# import de pandas

import pandas as pd

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/flower_color_symbolism.csv"

df = pd.read_csv(link)

app2 = Flask(__name__)
api2 = Api(app2)

# création d'une colonne pour le dataframe
df['color'] = df['Flower Color '].apply(lambda x: x.split(' ')[0])

# création d'une fonction qui affiche le texte d'une couleur quand il prend en paramètre cette couleur

def show_color(couleur):
    # On récupère la ligne dans laquelle le data frame est de la couleur souhaitée et on affiche uniquement la colonne Meaning
    return df['Meaning'].loc[df['color'] == couleur].iloc[0]

# Nous ajoutons le paramètre "forname" à la fonction get. 
# Puis nous utilisons ce paramètre pour retourner une phrase personalisée
class my_API_class(Resource):
       
    def get(self, var):
        return {var: show_color(var), 'Current_date': dt.date.today().strftime('%Y-%m-%d')}

# Nous devons indiquer comment va s'effectuer la requête.
# Concrètement, ce qui suivra l'URL de requête sera un string que nous nommerons comme une variable "forname".
# C'est cette variable qui est utilisée dans la fonction get.
api2.add_resource(my_API_class, '/<string:var>')

if __name__ == '__main__':
    app2.run(debug=True)



