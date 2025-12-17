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
  --backend-store-uri file:///home/ubuntu/MLflow/MLflow_lecture/mlruns \
  --default-artifact-root file:///home/ubuntu/MLflow/MLflow_lecture/mlruns \
  --serve-artifacts

/home/ubuntu/MLflow/MLflow_lecture/mlruns

# Compare le contenu des deux fichiers
diff -u src/train_model.py src/experiment.py

# ou 
diff -u src/train_model.py src/experiment.py

# Si pour une raison quelconque vous perdez la connexion à la machine virtuelle, il est possible qu'en vous y reconnectant, le serveur de tracking soit toujours en cours d'exécution. Dans ce cas, vous pouvez utiliser les commandes suivantes:

# Afficher les processus en cours sur le port 8080
lsof -i:8080

# Arrêter les processus en cours sur le port 8080
kill -9 $(lsof -t -i:8080)

# exécuter le script src/get_mlflow_env.py
python3 src/get_mlflow_env.py

# arborescence
tree -L 2

#  lancer notre projet MLflow
mlflow run ./src --experiment-id 284114746407137540 --run-name first_run_reproduced --env-manager=local
mlflow run ./src --experiment-id 284114746407137540 --run-name first_run_reproduced --env-manager=conda

# Note : Trouver et arrêter le processus sur le port 8080
sudo lsof -i :8080

sudo kill -9 <PID>

## 4

# 
python3 src/06_load_from_mlflow_model.py

# Pour lancer un serveur MLflow qui expose votre modèle via une API REST
#EXPERIMENT_ID = '284114746407137540'
#RUN_ID = 'acde7e1cc3ba4d059c0aed9cdab20fa0'
mlflow models serve \
        --model-uri '/home/ubuntu/MLflow/MLflow_lecture/mlruns/284114746407137540/acde7e1cc3ba4d059c0aed9cdab20fa0/artifacts/rf_apples' \
        --port 5002 \
        --host 0.0.0.0 \
        --env-manager local

# test de l'API
curl http://localhost:5002/invocations -H 'Content-Type: application/json' -d '{ "dataframe_records": [{"average_temperature":30.58472685635918, "rainfall":"6.786844618818696", "weekend":"0", "holiday":0, "price_per_kg":2.5024636658836807, "promo":0, "previous_days_demand":844.9940172482485}] }'

#
python3 src/07_test_api.py

## 5

#
python3 src/08_register_model.py \
            --tracking_uri "http://127.0.0.1:8080" \
            --experiment_name "Apple_Models" \
            --model_name "apple_demand_predictor"



# Déploiement de la version 1
python3 src/09_serve_registry_model.py \
    --tracking_uri "http://127.0.0.1:8080" \
    --model_name "apple_demand_predictor" \
    --version 1 \
    --port 5002


# test de la version 1 (dans un autre terminal)
python3 src/07_test_api.py