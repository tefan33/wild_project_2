import streamlit as st
import seaborn as sns
# import pandas as pd



# On récupère les dataset de sns
sns.get_dataset_names()
# on récupère le dataset taxi

taxis_df = sns.load_dataset("taxis")

taxis_df.head()

# on récupère la liste des zones possibles en supprimant les NAN. On récupère donc les valeurs non nulles et on prend la colonne 
liste_nom = taxis_df[taxis_df['pickup_borough'].notna()]['pickup_borough'].unique()

liste_nom.sort()

st.title("Bienvenu sur le site web de STEPHAN")

# on affiche une liste de choix avec la liste crée depuis la base de donnée
choix = st.selectbox("Veuillez choisir la photo que vous voulez\
                      afficher :", liste_nom)

# liste des choix d'images selon le choix de l'utilsateur
# Manhattan
# Queens
# nan
# Bronx
# Brooklyn

# afficher le choix
st.text("Tu as choisi le lieu :")
st.text(choix)

if choix == 'Manhattan':
    lien_image = "https://images.unsplash.com/photo-1555397430-57791c75748a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
elif choix == 'Queens':
    lien_image = "https://plus.unsplash.com/premium_photo-1720594170163-6514b14465d0?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
elif choix == 'Brooklyn':
    lien_image = "https://images.unsplash.com/photo-1525095240410-9645dea911e4?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
elif choix == 'Bronx':
    lien_image = "https://plus.unsplash.com/premium_photo-1673453455523-7390933a58f2?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
elif choix == 'nan':
    lien_image = "https://plus.unsplash.com/premium_photo-1682310096066-20c267e20605?q=80&w=1824&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
else:
    lien_image = "https://plus.unsplash.com/premium_photo-1682310096066-20c267e20605?q=80&w=1824&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# utilisation de la variable pour afficher l'image en question
st.image(lien_image)
