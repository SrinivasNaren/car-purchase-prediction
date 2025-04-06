📌 Objective:
To predict how much a customer is likely to spend on a car, using machine learning, based on their age, salary, credit card debt, and net worth.

📂 Dataset Info:
The dataset includes:

Customer name, email (removed later)

Country, gender, age

Annual salary 💰

Credit card debt 💳

Net worth 💼

Car purchase amount 🚗 (this is what we try to predict)

🧹 Data Preprocessing:

Removed unnecessary columns like customer name and email (they are not useful for prediction).

Removed any missing or empty values from the data.

Converted text columns (like gender, country) into numbers using One-Hot Encoding so the machine learning model can understand them.

🤖 Model Used:

Chose Linear Regression, a simple and commonly used machine learning algorithm.

It learns the relationship between a person’s financial data and the car price they paid.

🧪 Training and Testing:

Split the data into training (80%) and testing (20%) parts.

Trained the model using the training data.

Tested the model on new data it hasn’t seen before.

📈 Model Evaluation:

Measured how good the model is using:

R² Score: tells how accurate our predictions are.

MSE (Mean Squared Error): shows how far off our predictions are from real values.

📊 Visualization:

Plotted a graph between Actual Car Prices and Predicted Car Prices to see how close they are.

Helps us visually understand model performance.

✅ Conclusion:

Successfully created a machine learning model that can predict how much a customer might spend on buying a car.

This kind of model can be used in car dealerships, banks, or marketing to understand customers better.

