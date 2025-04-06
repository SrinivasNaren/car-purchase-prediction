# Importing tools
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the CSV file with correct encoding (fixing the unicode issue)
data = pd.read_csv('car_purchasing.csv', encoding='latin1')

# Display the column names
print("Columns in the dataset:", data.columns.tolist())

# View first few rows of data
print("First 5 rows of the dataset:")
print(data.head())

# Remove unnecessary columns like customer name and email
data = data.drop(['customer name', 'customer e-mail'], axis=1)

# Drop missing values if any
data = data.dropna()

# Convert categorical values (like gender, country) into numbers using one-hot encoding
data = pd.get_dummies(data, drop_first=True)

# Separate input (features) and output (target)
X = data.drop('car purchase amount', axis=1)
y = data['car purchase amount']

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# Show model performance
print("Accuracy (R2 score):", r2_score(y_test, y_pred))
print("Error (MSE):", mean_squared_error(y_test, y_pred))

# Plot actual vs predicted
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Car Purchase Amount")
plt.ylabel("Predicted Car Purchase Amount")
plt.title("Actual vs Predicted Car Purchase Amount")
plt.grid(True)
plt.show()
