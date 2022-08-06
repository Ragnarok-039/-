from selenium import webdriver
import time

link = "https://yandex.ru/"

try:
    browser = webdriver.Chrome()

    # Зайти на yandex.ru
    browser.get(link)

    time.sleep(3)

    # Ищем ссылку на «Картинки» и кликаем на нее.
    button = browser.find_element_by_link_text("Картинки")
    button.click()

    time.sleep(3)

    # Открыть 1 категорию, проверить что открылась, в поиске верный текст.
    # На данном этапе возникли трудности в поиске правильной ссылки на 1 категорию. Было опробовано много вариантов,
    # но увы.
    # К сожалению, отведенного времени не хватило на поиск решения.
    # На данном этапе на этом шаге необходимо больше времени для решения проблемы.
    button_2 = browser.find_element_by_css_selector(".PopularRequestList-Item.PopularRequestList-Item_pos_0 a")
    # print(button_2)
    button_2.click()

    time.sleep(3)

finally:
    # Закрываем браузер.
    browser.quit()
