import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data\house_data.csv")

# Features and Target
X = df[["area"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Test prediction
sample_area = [[1500]]
prediction = model.predict(sample_area)

print("Prediction for 1500 sq ft:", prediction[0])

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as model.pkl")