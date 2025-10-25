from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def setup_driver(headless=False):
    """
    Configura y devuelve un Chrome WebDriver (maximizado).
    Se puede ejecutar en modo headless si se pasa True.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # Usa chromedriver del PATH o Chrome for Testing
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)
    return driver
