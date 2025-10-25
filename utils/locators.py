from selenium.webdriver.common.by import By

class SauceLocators:
    # Pagina de login
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # Pagina de inventario
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    FIRST_ITEM_NAME = (By.XPATH, "(//div[@class='inventory_item_name'])[1]")
    FIRST_ITEM_PRICE = (By.XPATH, "(//div[@class='inventory_item_price'])[1]")
    FIRST_ADD_TO_CART_BTN = (By.XPATH, "(//button[text()='Add to cart'])[1]")

    # Pagina del carrito
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_IN_CART_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_IN_CART_PRICE = (By.CLASS_NAME, "inventory_item_price")
