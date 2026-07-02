from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
X, y = fetch_california_housing(return_X_y=True)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create StandardScaler object
scaler = StandardScaler()

# Fit scaler on training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data using the same scaler
X_test_scaled = scaler.transform(X_test)

# Create KNN model
model = KNeighborsRegressor(n_neighbors=5)

# Train model
model.fit(X_train_scaled, y_train)

# Predict on test data
predictions = model.predict(X_test_scaled)

# Evaluate model
print("R2 Score:", r2_score(y_test, predictions))
print("Mean Squared Error:", mean_squared_error(y_test, predictions))

# First 5 predictions
print("\nFirst 5 Predictions:")
print(predictions[:5])