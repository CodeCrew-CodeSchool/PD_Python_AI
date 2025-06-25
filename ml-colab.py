# Install dependencies and get data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes
# Verify Access to data and explore its contents

# Dataset definitions and descriptions can be found in the scikit-learn documentation here: https://scikit-learn.org/stable/datasets/toy_dataset.html under section 7.1.2
# https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

# loading data in memory and storing it in a pandas dataframe
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
# print(diabetes.values())

# Calling head to display first 5 rows with columns
print(data.head(), "\n")

# Column Definitions
# age
# sex
# bmi: body mass index
# bp: average blood pressure
# s1: tc, total serum cholesterol
# s2: ldl, low-densisty lipoproteins
# s3: hdl, high-density lipoproteins
# s4: tch, total cholestoerol / HDL
# s5: ltg, log of serum triglycerides level
# s6: glu, blood sugar level

# Note: Each of these 10 feature variables have been mean centered and scaled by the standard deviation times the square root of n_samples (i.e. the sum of squares of each column totals 1).


# Summary statistics
print("Summary Statistics\n", data.describe())

# Identify Target
data["1yr_disease_progression"] = diabetes.target

# Create variables to to define features and target
print(data)
X = data[["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"]]
Y = data["1yr_disease_progression"]

# Separate data into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=901)

# Model
model = LinearRegression()
model.fit(X_train, Y_train)



# Make a prediction
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)

r2 = r2_score(Y_test, Y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_pred)
plt.xlabel('Actual Target')
plt.ylabel('Predicted Target')
plt.title('Actual vs Predicted Targets')
# plot the line and the scatter of actual test results
plt.plot([min(Y_test), max(Y_test)], [min(Y_test), max(Y_test)], color='blue')
plt.show()