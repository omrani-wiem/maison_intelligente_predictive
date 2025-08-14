import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("house_data.csv")
X = df[['Temp', 'Light', 'Motion']]
y = df['Action']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Score sur test :", model.score(X_test, y_test))

# Sauvegarder modèle
with open("ml_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Modèle sauvegardé dans ml_model.pkl")
