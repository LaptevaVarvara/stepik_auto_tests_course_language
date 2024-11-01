from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.get(link)
    len_button = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    time.sleep(30)
    assert len_button > 0, "Element not found"
