import time
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

base_url="https://fyl.vqr.mybluehost.me/"

@pytest.mark.parametrize(("name", "email", "subject", "message"),
                         [
                             ("Vladimir", "Vladimir@gmail.com", "DDD", "Hello")
                         ])
@pytest.mark.alhymrec
def test_alhymrec(browser_firefox, name, email, subject, message):
    browser_firefox.get(base_url)
    #browser.find_element(By.CSS_SELECTOR, "body div:nth-child(51) .play").click()
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ARTISTS"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ARTISTS LIST"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ELEMENTS"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ABOUT US"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "ABOUT – EXEMPLE 1"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CONTACT"))).click()
    time.sleep(5)
    WebDriverWait(browser_firefox, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "CONTACT 1"))).click()
    browser_firefox.find_element(By.NAME, "your-name").send_keys(name)
    browser_firefox.find_element(By.NAME, "your-email").send_keys(email)
    browser_firefox.find_element(By.NAME, "your-subject").send_keys(subject)
    browser_firefox.find_element(By.NAME, "your-message").send_keys(message)
    browser_firefox.find_element(By.CSS_SELECTOR, "label > input[name='_mc4wp_subscribe_contact-form-7']").click()
    browser_firefox.find_element(By.CSS_SELECTOR, ".has-spinner.wpcf7-form-control.wpcf7-submit").click()
