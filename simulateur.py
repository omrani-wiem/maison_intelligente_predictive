import random
import pandas as pd

pieces = ['Salon', 'Chambre', 'Cuisine']

def generer_donnees(nb=100):
    data = []
    for _ in range(nb):
        for piece in pieces:
            temp = random.randint(15, 30)
            light = random.randint(0, 100)
            motion = random.randint(0, 1)
            action = 1 if temp < 20 else 0  # 1 = chauffage allumé
            data.append([piece, temp, light, motion, action])
    df = pd.DataFrame(data, columns=['Piece', 'Temp', 'Light', 'Motion', 'Action'])
    df.to_csv("house_data.csv", index=False)
    print("Données générées pour les pièces et sauvegardées dans house_data.csv")

generer_donnees()
