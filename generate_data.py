import pandas as pd
import numpy as np

# pandas : construire et manipuler le tableau
# numpy : générer des valeurs aléatoires

# Graine aléatoire pour garantir la reproductibilité
np.random.seed(42)

n = 500  # Nombre de clients fictifs

# Chaque colonne est une FEATURE (donnée d'entrée du modèle)
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "salaire": np.random.randint(1200, 8000, n),
    "abonnement": np.random.choice(["Basique", "Standard", "Premium"], n),
    "anciennete": np.random.randint(0, 15, n),
    "consommation": np.random.randint(0, 100, n)
})

# TARGET (colonne à prédire) : churn
# Un client peu actif (consommation < 30)
# ET récent (ancienneté < 2 ans) est considéré à risque de départ.
data["churn"] = (
    (data["consommation"] < 30) &
    (data["anciennete"] < 2)
).astype(int)

# Sauvegarde dans un fichier CSV
data.to_csv("churn_data.csv", index=False)

# Affichages de contrôle
print(data.head())

print(f"Taux de churn : {data['churn'].mean():.1%}")