from selenium import webdriver
import time

link = "https://yandex.ru/"

try:
    browser = webdriver.Chrome()

    # Зайти на yandex.ru
    browser.get(link)

    # Проверить наличие поля поиска.
    find_field = browser.find_element_by_class_name("input__control.input__input.mini-suggest__input")

    # Если поле поиска найдено, ввести в него "Тензор".
    if find_field:
        find_field.send_keys("Тензор")

    # Проверить всплывающее окно с подсказками.
    suggest = browser.find_element_by_class_name("mini-suggest__popup-content")

    # Если всплывающее окно найдено, вывести соответствующее сообщение в консоль.
    if suggest:
        print("Появилась таблица с подсказками (suggest).")
    else:
        print("Не появилась таблица с подсказками (suggest).")

    time.sleep(3)

    # Ищем и нажимаем кнопку "Найти".
    button = browser.find_element_by_class_name("button.mini-suggest__button.button_theme_search.button_size_search.i-bem.button_js_inited")
    button.click()

    # Проверяем, появились ли результаты поиска.
    result = browser.find_element_by_class_name("serp-list.serp-list_left_yes")
    # Если появились, выводим соответсвующее сообщение в консоль.
    if result:
        print("Появилась таблица результатов поиска.")
    else:
        print("Не появилась таблица результатов поиска.")

    # Ищем первую ссылку из поиска и проверяем то, что она содержит фразу "Тензор".
    link = browser.find_element_by_css_selector("div.Organic.organic.Typo.Typo_text_m.Typo_line_s.i-bem")
    document = link.text.split()
    # print(link)
    # print(document)
    # Если содержит вышеуказанную фразу, выводим в консоль соответсвующее сообщение.
    if "Тензор" in document:
        print("Первая ссылка содержит поисковой запрос 'Тензор'.")
    else:
        print("Первая ссылка не содержит поисковой запрос 'Тензор'.")

    time.sleep(3)

finally:
    # Закрываем браузер.
    browser.quit()
