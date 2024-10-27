from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_from_directory
import os

# Load and preprocess the dataset
data = pd.read_csv('Liver Patient Dataset (LPD)_train.csv', encoding='latin1')
data.columns = data.columns.str.strip()

# Define features and target
X = data.drop(['Total Bilirubin', 'Result', 'Gender of the patient'], axis=1)
y = data['Total Bilirubin']

# Handle missing values
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train models
linear_reg = LinearRegression()
random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
linear_reg.fit(X_train, y_train)
random_forest.fit(X_train, y_train)

# Predictions and metric calculations
y_pred_lr = linear_reg.predict(X_test)
y_pred_rf = random_forest.predict(X_test)

# Metrics for Linear Regression
metrics_lr = {
    'R²': r2_score(y_test, y_pred_lr),
    'MSE': mean_squared_error(y_test, y_pred_lr),
    'MAE': mean_absolute_error(y_test, y_pred_lr)
}

# Metrics for Random Forest
metrics_rf = {
    'R²': r2_score(y_test, y_pred_rf),
    'MSE': mean_squared_error(y_test, y_pred_rf),
    'MAE': mean_absolute_error(y_test, y_pred_rf)
}

# Plotting function to compare metrics
def create_comparison_plot(metrics_lr, metrics_rf, save_path="static/comparison_plot.png"):
    metrics = ['R²', 'MSE', 'MAE']
    linear_metrics = [metrics_lr['R²'], metrics_lr['MSE'], metrics_lr['MAE']]
    random_forest_metrics = [metrics_rf['R²'], metrics_rf['MSE'], metrics_rf['MAE']]

    x = np.arange(len(metrics))  # label locations
    width = 0.35  # width of the bars

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, linear_metrics, width, label='Linear Regression', color='blue')
    plt.bar(x + width/2, random_forest_metrics, width, label='Random Forest', color='green')

    # Add labels and title
    plt.xlabel('Metrics')
    plt.title('Comparison of Linear Regression vs Random Forest')
    plt.xticks(x, metrics)
    plt.legend()

    # Save the plot
    plt.savefig(save_path)
    plt.close()

# Initialize Flask app
app = Flask(__name__)

# Route to serve the plot image
@app.route('/static/<path:filename>')
def static_file(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    # Generate the comparison plot and save it as an image
    plot_path = "static/comparison_plot.png"
    create_comparison_plot(metrics_lr, metrics_rf, save_path=plot_path)

    # Pass metrics and image path to the template
    return render_template('index.html', metrics_lr=metrics_lr, metrics_rf=metrics_rf, plot_url=plot_path)

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
