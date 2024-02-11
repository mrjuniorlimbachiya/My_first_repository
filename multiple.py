import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("climate_change.csv")

# Assuming your dataset has columns 'X1', 'X2', 'X3', and 'Y'
X = df[['Month', 'MEI', 'CO2', 'CH4', 'N2O', 'CFC-11','CFC-12', 'TSI', 'Aerosols', 'Year']]
Y = df['Temp']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Print the coefficients and intercept
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Plot the regression line for one variable (e.g., X1)
plt.scatter(X_test['Year'], Y_test, color='black', label='Actual data')
plt.plot(X_test['Year'], Y_pred, color='red', linewidth=3, label='Regression line')
plt.xlabel('Year')
plt.ylabel('Temp')
plt.legend()
plt.title('Multiple Regression with Regression Line')
plt.show()