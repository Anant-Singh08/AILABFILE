import pandas as pd

data = {
    "Name": ["Anant Singh", "Shabd Kumar", "Sumati Kumar"],
    "Age": [25, 30, 22],
    "City": ["Delhi", "Mumbai", "Bangalore"],
    "Salary": [50000, 70000, 60000],
    "Experience": [2, 5, 1]
}

df = pd.DataFrame(data)

df["Salary_Hike"] = df["Salary"] * 1.1
average_age = df["Age"].mean()
df_sorted = df.sort_values(by="Salary", ascending=False)
shabd_data = df[df["Name"] == "Shabd Kumar"]
city_counts = df["City"].value_counts()
df["Salary_Category"] = pd.cut(df["Salary"], bins=[0, 55000, 65000, 75000], labels=["Low", "Medium", "High"])
grouped_by_city = df.groupby("City").agg({"Salary": ["mean", "max"], "Age": "mean"})

high_salary_filter = df[df["Salary"] > 55000]

print("Original DataFrame:\n", df)
print("\nAverage Age:", average_age)
print("\nDataFrame sorted by Salary:\n", df_sorted)
print("\nData for Shabd Kumar:\n", shabd_data)
print("\nCount of individuals by City:\n", city_counts)
print("\nSalary Category:\n", df[["Name", "Salary", "Salary_Category"]])
print("\nGrouped by City:\n", grouped_by_city)
print("\nIndividuals with Salary > 55000:\n", high_salary_filter)
