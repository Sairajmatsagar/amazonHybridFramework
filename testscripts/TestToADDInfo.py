import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()

@pytest.mark.usefixtures("setup_and_teardown")
def test_to_verify_my_info_element_clickable_or_not():
    driver.find_element(By.NAME, 'username').send_keys("ADMIN")
    driver.find_element(By.NAME, 'password').send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert 'OrangeHRM'.__eq__(driver.title)
    driver.find_element(By.XPATH,"//span[text()='My Info']").click()
    assert 'OrangeHRM'.__eq__(driver.title)


@pytest.mark.usefixtures("setup_and_teardown")
def test_to_add_info():
    driver.find_element(By.NAME, 'username').send_keys("ADMIN")
    driver.find_element(By.NAME, 'password').send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert 'OrangeHRM'.__eq__(driver.title)
    driver.find_element(By.XPATH,"//span[text()='My Info']").click()
    assert 'OrangeHRM'.__eq__(driver.title)
    first_name = driver.find_element(By.NAME,'firstName')
    first_name.clear()
    first_name.send_keys("sairaj")
    first_name = driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
    first_name.clear()
    first_name.send_keys("sairaj")



