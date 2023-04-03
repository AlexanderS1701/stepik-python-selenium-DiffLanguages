import time

from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_find_addtocart_buttom(browser):
    browser.get(link)
    addtocart_buttom = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert addtocart_buttom is not None, f"Элемент с идентификатором {addtocart_buttom} не найден на странице"
    time.sleep(10)