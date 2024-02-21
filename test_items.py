import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def test_first(browser):
    browser.implicitly_wait(5)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element(By.CSS_SELECTOR,'button.btn-add-to-basket').click()
    sleep(5)

