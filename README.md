# 🚗 Car Purchase Prediction using Linear Regression

This project predicts the amount a customer is likely to spend on purchasing a car based on their personal and financial details. It uses **Linear Regression** to analyze the relationship between various features and the car purchase amount.

---

## 📊 Dataset Overview

The dataset includes the following columns:

- `customer name`
- `customer e-mail`
- `country`
- `gender`
- `age`
- `annual Salary`
- `credit card debt`
- `net worth`
- `car purchase amount` (Target)

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn (sklearn)

---

## 📁 Project Structure

```
car-purchase-prediction/
│
├── car_purchasing.csv          # Dataset file
├── main.py                     # Main code for training & prediction
└── README.md                   # This file
```

---

## 🧠 Steps Performed

1. **Load the dataset** using Pandas
2. **Clean the data** by removing unnecessary columns and handling missing values
3. **Encode categorical variables** (e.g., country, gender)
4. **Split the dataset** into training and test sets
5. **Train the Linear Regression model**
6. **Evaluate the model** using R² score and Mean Squared Error
7. **Plot Actual vs Predicted values** using Matplotlib

---

## 🚀 How to Run the Project

### ✅ Prerequisites

- Python 3.x installed
- Libraries: `pandas`, `matplotlib`, `scikit-learn`

You can install required libraries using:

```bash
pip install pandas matplotlib scikit-learn
```

### ▶️ Run the Code

```bash
python main.py
```

It will show:

- Accuracy (R2 score)
- Error (Mean Squared Error)
- A scatter plot of actual vs predicted values

---

## 📷 Sample Output

You’ll get a plot like this:

![Output Graph](output.png)

---

## 🙌 Contribution

Feel free to fork the repo and open a Pull Request for any improvements or suggestions.

---

## 📬 Contact

Created by [V Srinivas Naren](https://github.com/SrinivasNaren)

---
