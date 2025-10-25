from selenium.webdriver.common.by import By


class SauceLocators:
    """ login page """
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")

    """ inventory page """
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")

    """ busca el primer elemento que tenga un data-test="inventory-item-name" """
    FIRST_ITEM_NAME = (
        By.XPATH, "(//div[@data-test='inventory-item-name'])[1]")

    """ busca el primer elemento que tenga un data-test="inventory-item-price" """
    FIRST_ITEM_PRICE = (
        By.XPATH, "(//div[@data-test='inventory-item-price'])[1]")

    """ busca el primer botón cuyo data-test *comience con* "add-to-cart-" """
    FIRST_ADD_TO_CART_BTN = (
        By.XPATH, "(//button[starts-with(@data-test, 'add-to-cart-')])[1]")

    """ cart page """
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    """ usamos data-test aquí también para más estabilidad """
    ITEM_IN_CART_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_IN_CART_PRICE = (
        By.CSS_SELECTOR, "[data-test='inventory-item-price']")
