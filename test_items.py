from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_button_in_store_page(browser):
    browser.get(url)
    button_add = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button_add.is_displayed(), \
        'Кнопка добавления товара отсутсвует'
