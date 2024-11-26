from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Nous ajoutons le paramètre "forname" à la fonction get. 
# Puis nous utilisons ce paramètre pour retourner une phrase personalisée
class my_API_class(Resource):
    def get(self, forname):
        sentence = 'Hi ' + forname + ', welcome in my API'
        return {'hello': sentence}

# Nous devons indiquer comment va s'effectuer la requête.
# Concrètement, ce qui suivra l'URL de requête sera un string que nous nommerons comme une variable "forname".
# C'est cette variable qui est utilisée dans la fonction get.
api.add_resource(my_API_class, '/<string:forname>')

if __name__ == '__main__':
    app.run(debug=True)