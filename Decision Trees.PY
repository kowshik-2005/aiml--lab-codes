from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create and train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Make a prediction
prediction = model.predict(np.array([[5.0, 3.5, 1.0, 0.2]]))
print(f"Prediction for input [5.0, 3.5, 1.0, 0.2]: {prediction[0]}")
