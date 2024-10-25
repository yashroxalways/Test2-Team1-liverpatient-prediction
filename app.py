from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('/content/Liver Patient Dataset (LPD)_train.csv', encoding='latin1')

# Clean column names (removing leading/trailing spaces)
data.columns = data.columns.str.strip()

# Define the target variable (for example, 'Total Bilirubin') and features
X = data.drop(['Total Bilirubin', 'Result', 'Gender of the patient'], axis=1)
y = data['Total Bilirubin']

# Handle any missing values (if any)
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the models
linear_reg = LinearRegression()
random_forest = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the models
linear_reg.fit(X_train, y_train)
random_forest.fit(X_train, y_train)

# Make predictions
y_pred_lr = linear_reg.predict(X_test)
y_pred_rf = random_forest.predict(X_test)

# Calculate metrics (R², MSE, MAE)
r2_lr = r2_score(y_test, y_pred_lr)
r2_rf = r2_score(y_test, y_pred_rf)
mse_lr = mean_squared_error(y_test, y_pred_lr)
mse_rf = mean_squared_error(y_test, y_pred_rf)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
mae_rf = mean_absolute_error(y_test, y_pred_rf)

# Print the metrics for both models
print(f"Linear Regression - \nR²: {r2_lr:.4f}, \nMSE: {mse_lr:.4f}, \nMAE: {mae_lr:.4f}")
print()
print()
print(f"Random Forest Regression - \nR²: {r2_rf:.4f}, \nMSE: {mse_rf:.4f}, \nMAE: {mae_rf:.4f}")
print()
print()

# Create a bar plot for comparison of metrics
metrics = ['R²', 'MSE', 'MAE']
linear_metrics = [r2_lr, mse_lr, mae_lr]
random_forest_metrics = [r2_rf, mse_rf, mae_rf]

x = np.arange(len(metrics))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 5))

# Plotting bars for Linear Regression and Random Forest
rects1 = ax.bar(x - width/2, linear_metrics, width, label='Linear Regression', color='blue')
rects2 = ax.bar(x + width/2, random_forest_metrics, width, label='Random Forest', color='green')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Metrics')
ax.set_title('Comparison of Linear Regression vs Random Forest Regression')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

# Display the values on top of the bars
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()
