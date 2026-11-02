
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    file_path = Path("index.html").resolve().as_uri()
    driver.get(file_path)

    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("20")
    driver.find_element(By.ID, "addBtn").click()

    result = driver.find_element(By.ID, "result").text

    print("Actual Output:", result)

    assert result == "Result: 30"
    print("Test Passed")
finally:
    driver.quit()
