from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the Flask app
url = "http://127.0.0.1:5000/"

# Initialize WebDriver (Chrome, change for Firefox if needed)
driver = webdriver.Chrome()

try:
    # Open the Flask app
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Locate and retrieve metric elements
    lr_r2 = driver.find_element(By.XPATH, "//p[strong[text()='R²:']]").text
    lr_mse = driver.find_element(By.XPATH, "//p[strong[text()='MSE:']]").text
    lr_mae = driver.find_element(By.XPATH, "//p[strong[text()='MAE:']]").text
    rf_r2 = driver.find_element(By.XPATH, "(//p[strong[text()='R²:']])[2]").text
    rf_mse = driver.find_element(By.XPATH, "(//p[strong[text()='MSE:']])[2]").text
    rf_mae = driver.find_element(By.XPATH, "(//p[strong[text()='MAE:']])[2]").text

    # Print values for verification
    print("Linear Regression Metrics")
    print(lr_r2, lr_mse, lr_mae)
    print("Random Forest Metrics")
    print(rf_r2, rf_mse, rf_mae)

    # Verify if values are displayed
    assert "R²:" in lr_r2, "Linear Regression R² not displayed!"
    assert "MSE:" in lr_mse, "Linear Regression MSE not displayed!"
    assert "MAE:" in lr_mae, "Linear Regression MAE not displayed!"
    assert "R²:" in rf_r2, "Random Forest R² not displayed!"
    assert "MSE:" in rf_mse, "Random Forest MSE not displayed!"
    assert "MAE:" in rf_mae, "Random Forest MAE not displayed!"

    print("All metrics displayed correctly.")

except AssertionError as e:
    print(f"Test failed: {e}")

finally:
    # Close the browser
    driver.quit()
