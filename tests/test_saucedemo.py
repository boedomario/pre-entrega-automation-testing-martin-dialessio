import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_helper import setup_driver
from utils.locators import SauceLocators

BASE_URL = "https://www.saucedemo.com"
USER = "standard_user"
PASS = "secret_sauce"

# Fixture base
@pytest.fixture(scope="function")
def driver():
    """Inicia y cierra el navegador, sin login."""
    drv = setup_driver(headless=False)
    yield drv
    print("\nCerrando navegador...")
    drv.quit()

# Fixture con login
@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Realiza el login y deja el navegador en la pagina de inventario."""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located(SauceLocators.USERNAME_INPUT)).send_keys(USER)
    driver.find_element(*SauceLocators.PASSWORD_INPUT).send_keys(PASS)
    driver.find_element(*SauceLocators.LOGIN_BUTTON).click()

    wait.until(EC.url_contains("/inventory.html"))
    wait.until(EC.visibility_of_element_located(SauceLocators.PAGE_TITLE))
    yield driver

# Test de login
@pytest.mark.login
def test_login_exitoso(driver):
    """Login correcto con validacion de URL y titulo."""
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located(SauceLocators.USERNAME_INPUT)).send_keys(USER)
    driver.find_element(*SauceLocators.PASSWORD_INPUT).send_keys(PASS)
    driver.find_element(*SauceLocators.LOGIN_BUTTON).click()

    wait.until(EC.url_contains("/inventory.html"))
    title = wait.until(EC.visibility_of_element_located(SauceLocators.PAGE_TITLE)).text

    assert "/inventory.html" in driver.current_url
    assert title == "Products"
    print("Login exitoso y pagina de inventario visible.")

# Test de catalogo
@pytest.mark.catalogo
def test_verificacion_catalogo(logged_in_driver):
    """Verifica que el catalogo se cargue y muestre los productos."""
    driver = logged_in_driver
    assert driver.find_element(*SauceLocators.PAGE_TITLE).text == "Products"

    products = driver.find_elements(*SauceLocators.INVENTORY_ITEM)
    assert len(products) > 0, "No se encontraron productos"

    name = driver.find_element(*SauceLocators.FIRST_ITEM_NAME).text
    price = driver.find_element(*SauceLocators.FIRST_ITEM_PRICE).text

    assert name and price, "Nombre o precio vacio"
    print(f"Primer producto: {name} - Precio: {price}")

# Test de carrito
@pytest.mark.carrito
def test_agregar_producto_y_verificar(logged_in_driver):
    """Agrega un producto al carrito y verifica nombre y precio."""
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located(SauceLocators.INVENTORY_ITEM))
    first_name = driver.find_element(*SauceLocators.FIRST_ITEM_NAME).text
    first_price = driver.find_element(*SauceLocators.FIRST_ITEM_PRICE).text

    driver.find_element(*SauceLocators.FIRST_ADD_TO_CART_BTN).click()
    badge = wait.until(EC.visibility_of_element_located(SauceLocators.CART_BADGE))
    assert badge.text == "1"

    driver.find_element(*SauceLocators.CART_LINK).click()
    cart_name = wait.until(EC.visibility_of_element_located(SauceLocators.ITEM_IN_CART_NAME)).text
    cart_price = driver.find_element(*SauceLocators.ITEM_IN_CART_PRICE).text

    assert cart_name == first_name, "El nombre del producto no coincide"
    assert cart_price == first_price, "El precio del producto no coincide"
    print(f"Producto agregado correctamente: {cart_name}")
