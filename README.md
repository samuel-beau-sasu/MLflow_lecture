# MLflow

For the MLflow course.

#  environnement virtuel 
source env_mlflow/bin/activate

# activer conda
eval "$(/home/ubuntu/miniconda3/bin/conda shell.bash hook)"

# désactiver conda 
conda deactivate

# lister les environnements
conda env list

# lancer MLflow en local en exécutant la commande suivante dans le terminal 

mlflow server \
  --host 0.0.0.0 \
  --port 8080 \
  --backend-store-uri file:///home/ubuntu/MLflow_Course/mlruns \
  --default-artifact-root file:///home/ubuntu/MLflow_Course/mlruns \
  --serve-artifacts

# Compare le contenu des deux fichiers
diff -u src/train_model.py src/experiment.py

# ou 
diff -u src/train_model.py src/experiment.py

# Si pour une raison quelconque vous perdez la connexion à la machine virtuelle, il est possible qu'en vous y reconnectant, le serveur de tracking soit toujours en cours d'exécution. Dans ce cas, vous pouvez utiliser les commandes suivantes:

# Afficher les processus en cours sur le port 8080
lsof -i:8080

# Arrêter les processus en cours sur le port 8080
kill -9 $(lsof -t -i:8080)