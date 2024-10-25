from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Specify the path to the ChromeDriver executable
chromedriver_path = './chromedriver'  # Update this if necessary
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Initialize the Chrome driver
driver = webdriver.Chrome(chromedriver_path)

try:
    # Open the Flask app
    driver.get("http://127.0.0.1:5000/")

    # Find the file upload element and upload a CSV file
    upload_element = driver.find_element(By.NAME, "file")
    upload_element.send_keys(os.path.abspath("sample_data.csv"))  # Update the filename if necessary

    # Submit the form
    upload_element.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(5)  # Adjust this delay if necessary

    # Check for expected results
    # Replace these with actual values from your CSV file and expected outputs
    r2_lr = driver.find_element(By.XPATH, "//p[contains(text(), 'R²:')]").text
    mse_lr = driver.find_element(By.XPATH, "//p[contains(text(), 'MSE:')]").text
    mae_lr = driver.find_element(By.XPATH, "//p[contains(text(), 'MAE:')]").text

    print(f"Linear Regression Results: {r2_lr}, {mse_lr}, {mae_lr}")

    r2_rf = driver.find_element(By.XPATH, "//h3[following-sibling::p[contains(text(), 'R²:')]]").text
    mse_rf = driver.find_element(By.XPATH, "//h3[following-sibling::p[contains(text(), 'MSE:')]]").text
    mae_rf = driver.find_element(By.XPATH, "//h3[following-sibling::p[contains(text(), 'MAE:')]]").text

    print(f"Random Forest Results: {r2_rf}, {mse_rf}, {mae_rf}")

    # Verify that results are displayed (you can add more specific assertions as needed)
    assert "R²:" in r2_lr
    assert "MSE:" in mse_lr
    assert "MAE:" in mae_lr
    assert "R²:" in r2_rf
    assert "MSE:" in mse_rf
    assert "MAE:" in mae_rf

finally:
    # Close the browser
    driver.quit()
