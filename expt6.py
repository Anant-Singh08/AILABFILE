import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["Anant Singh", "Shabd Kumar", "Sumati Kumar", "Raj Mehta", "Priya Sharma", "Aditi Verma", 
             "Vikram Joshi", "Ravi Singh", "Neha Bansal", "Sneha Gupta"],
    "Experience": [2, 5, 1, 4, 3, 6, 7, 1, 8, 2],
    "Salary": [50000, 70000, 60000, 65000, 55000, 80000, 95000, 45000, 90000, 52000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

plt.scatter(X, y, color='blue', label='Actual Salaries')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.grid()
plt.show()

for name, exp, pred in zip(df["Name"], df["Experience"], model.predict(X)):
    print(f"Predicted Salary for {name} with {exp} years of experience: {pred:.2f}")
