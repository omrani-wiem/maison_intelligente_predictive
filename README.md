# maison_intelligente_predictive
Ce projet simule une maison intelligente capable de prédire si le chauffage doit être allumé ou éteint en fonction de la température, de la luminosité et du mouvement détecté dans chaque pièce.
Il utilise Python, Dash pour l’interface web et Machine Learning (arbre de décision) pour la prédiction.

Fonctionnalités:
Génération de données simulées pour chaque pièce (Salon, Chambre, Cuisine) : température, lumière, mouvement.
Entraînement d’un modèle ML pour prédire l’état du chauffage.
Interface web interactive avec Dash pour afficher les mesures et l’état du chauffage.
Bouton pour générer des lectures aléatoires en temps réel.

simulateur.py → génère des données aléatoires (house_data.csv).
ml_model.py → entraîne un modèle ML et le sauvegarde dans ml_model.pkl.
dashbord.py → charge le modèle et affiche les mesures et prédictions sur le dashboard.
