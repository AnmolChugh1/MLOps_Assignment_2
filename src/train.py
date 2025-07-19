import json
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Step 1: Load configuration
with open("../config/config.json", "r") as f:
    config = json.load(f)

# Step 2: Load dataset (using Iris for demonstration)
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=config["random_state"]
)

# Step 4: Initialize model with config parameters
model = LogisticRegression(
    penalty=config["penalty"],
    C=config["C"],
    solver=config["solver"],
    max_iter=config["max_iter"],
    random_state=config["random_state"]
)

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Save the trained model
joblib.dump(model, "model_train.pkl")

print("Model training complete. Saved as model_train.pkl.")
