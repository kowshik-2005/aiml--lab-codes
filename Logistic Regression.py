import numpy as np  # Import numpy
from sklearn.linear_model import LogisticRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])  # Features
y = np.array([0, 0, 1, 1, 1])  # Labels

# Logistic Regression
model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Prediction
print("Predictions:", y_pred)
