import mlflow
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. Loading data
# TODO: Replace with the path to your dataset
print("Loading data...")
data = pd.read_csv("data/fake_data.csv")
X = data.drop(columns=["date", "demand"])
X = X.astype('float')

# 2. Define the path to the MLflow model
# TODO: Replace with the path to your "rf_apples" folder created previously
EXPERIMENT_ID = '284114746407137540'
RUN_ID = 'acde7e1cc3ba4d059c0aed9cdab20fa0'
#model_path = ''  # For example: '/home/ubuntu/MLflow/MLflow_lecture/mlruns/{EXPERIMENT_ID}/{RUN_ID}/artifacts/rf_apples'
model_path = f"/home/ubuntu/MLflow/MLflow_lecture/mlruns/{EXPERIMENT_ID}/{RUN_ID}/artifacts/rf_apples"

# 3. Load the model
print("Loading model...")
model = mlflow.sklearn.load_model(model_path)

# 4. Make predictions on the entire dataset
print("Calculating predictions...")
predictions = model.predict(X)

# 5. Calculate and display the average of predictions
# Calculate the mean prediction
mean_prediction = predictions.mean()
print(mean_prediction)