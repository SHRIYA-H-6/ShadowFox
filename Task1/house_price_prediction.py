# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("HousingData.csv")

# Display first few rows
print(data.head())

# Handle missing values (fill with mean)
data = data.fillna(data.mean())

# Features (X) and Target (y)
X = data.drop("MEDV", axis=1)   # MEDV = house price
y = data["MEDV"]

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Example prediction
sample = X_test.iloc[0].values.reshape(1, -1)
predicted_price = model.predict(sample)

print("Sample Predicted Price:", predicted_price[0])