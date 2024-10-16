from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

model = LinearRegression()
model.fit(X, y)
prediction = model.predict(np.array([[6]]))
print(f"Prediction for input 6: {prediction[0]}")
