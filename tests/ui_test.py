from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

# Add Printer A
driver.find_element(By.CSS_SELECTOR, "button.add[data-id='printer-a']").click()
print("➡ Added Printer A to cart")

# Wait for total to update
WebDriverWait(driver, 5).until(
    lambda d: int(d.find_element(By.ID, "cart-total").text) == 150
)
print("✅ Cart total updated to $150")

# Remove Printer A
driver.find_element(By.CSS_SELECTOR, "button.remove[data-id='printer-a']").click()
WebDriverWait(driver, 5).until(
    lambda d: int(d.find_element(By.ID, "cart-total").text) == 0
)
print("✅ Cart total updated to $0 after removal")

driver.quit()
print("✅ Selenium test completed successfully")
