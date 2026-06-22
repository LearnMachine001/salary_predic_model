import pandas as pd
import numpy as np
import joblib

data = {
    "Experience":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "Salary":[25000,30000,35000,45000,55000,65000,75000,
            85000,95000,105000,115000,125000,135000,145000,155000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]


print(df)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error,r2_score

MAE = mean_absolute_error(y_test, y_pred)
R2_score = r2_score(y_test, y_pred)

print(f"Mean Absolute Error {MAE}")
print(f"R2 Score {R2_score}")

# user_input = int(input("Enter Experiance :"))

# prediction  = pd.DataFrame([user_input])


# print("Salary based on Experiance :",model.predict(prediction))

joblib.dump(model,"salary_model.pkl")
# joblib.dump(scaler,"scaler_model.pkl")