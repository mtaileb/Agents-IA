import plotly.graph_objects as go
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

documents = [
    "The sky is blue and beautiful.",
    "Love this blue and beautiful sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, eggs, toast, and beans",
    "I love green eggs, ham, sausages and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today",
    "The dog is lazy but the brown fox is quick!"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# --------------------------------------------
# AFFICHAGE DES VECTEURS
# --------------------------------------------

# 1. Afficher sous forme de tableau (DataFrame)
print("=" * 80)
print("VECTEURS TF-IDF DES DOCUMENTS")
print("=" * 80)

# Récupérer les noms des termes (mots)
feature_names = vectorizer.get_feature_names_out()

# Convertir la matrice en DataFrame pandas pour un affichage lisible
df_vecteurs = pd.DataFrame(
    X.toarray(),
    columns=feature_names,
    index=[f"Doc {i+1}" for i in range(len(documents))]
)

print("\n📊 Tableau des vecteurs TF-IDF (chaque ligne = un document) :")
print("-" * 80)
print(df_vecteurs)

# 2. Afficher la matrice sous forme de heatmap avec Plotly
print("\n" + "=" * 80)
print("VISUALISATION DE LA MATRICE TF-IDF (Heatmap)")
print("=" * 80)

fig = go.Figure(data=go.Heatmap(
    z=X.toarray(),
    x=feature_names,
    y=[f"Doc {i+1}" for i in range(len(documents))],
    colorscale='Viridis',
    hoverongaps=False,
    text=X.toarray(),
    texttemplate='%{text:.2f}',
    textfont={"size": 10}
))

fig.update_layout(
    title="Matrice TF-IDF - Heatmap",
    xaxis_title="Termes (mots)",
    yaxis_title="Documents",
    width=1200,
    height=600,
    xaxis={'tickangle': 45}
)

fig.show()

# 3. Afficher le nombre de termes et la taille de la matrice
print("\n" + "=" * 80)
print("INFORMATIONS SUR LA MATRICE")
print("=" * 80)
print(f"📝 Nombre de documents : {X.shape[0]}")
print(f"📝 Nombre de termes uniques : {X.shape[1]}")
print(f"📝 Taille de la matrice : {X.shape[0]} x {X.shape[1]}")

# 4. Afficher les termes (vocabulaire)
print("\n" + "=" * 80)
print("VOCABULAIRE (termes uniques)")
print("=" * 80)
for i, terme in enumerate(feature_names):
    print(f"  {i+1}. '{terme}'")

# 5. Afficher les vecteurs par document (plus détaillé)
print("\n" + "=" * 80)
print("VECTEURS PAR DOCUMENT (termes avec poids > 0)")
print("=" * 80)

for i, doc in enumerate(documents):
    print(f"\n📄 Document {i+1}: \"{doc}\"")
    print("-" * 60)
    
    # Récupérer les poids non nuls pour ce document
    doc_vector = X[i].toarray().flatten()
    termes_avec_poids = [(feature_names[j], doc_vector[j]) 
                         for j in range(len(feature_names)) 
                         if doc_vector[j] > 0]
    
    # Trier par poids décroissant
    termes_avec_poids.sort(key=lambda x: x[1], reverse=True)
    
    if not termes_avec_poids:
        print("  (aucun terme avec poids > 0)")
    else:
        for terme, poids in termes_avec_poids:
            print(f"  • '{terme}' : {poids:.4f}")
