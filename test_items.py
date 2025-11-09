import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button_exists(browser):
    """
    Тест проверяет наличие кнопки добавления товара в корзину
    на странице товара
    """
    # URL страницы товара
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    # Открыть страницу товара
    print(f"\n📖 Открытие страницы: {product_url}")
    browser.get(product_url)
    
    # Небольшая пауза для загрузки страницы
    time.sleep(2)
    
    # Найти кнопку добавления в корзину
    try:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        
        print(f"✅ Кнопка добавления в корзину найдена!")
        print(f"📋 Текст кнопки: '{add_to_cart_button.text}'")
        
        # Проверка, что кнопка видима
        assert add_to_cart_button.is_displayed(), \
            "❌ Кнопка добавления в корзину не отображается на странице"
        
        # Проверка, что кнопка доступна для клика
        assert add_to_cart_button.is_enabled(), \
            "❌ Кнопка добавления в корзину неактивна"
        
        print("✅ Тест пройден: кнопка добавления в корзину присутствует и доступна")
        
    except Exception as e:
        # Сохранить скриншот при ошибке
        browser.save_screenshot("error_screenshot.png")
        print(f"❌ Ошибка: {e}")
        raise AssertionError(
            "❌ Кнопка добавления в корзину не найдена на странице! "
            "Скриншот сохранен в error_screenshot.png"
        )
