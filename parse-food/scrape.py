import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

# сайт парсинга
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# создание заголовков для безопасности
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

# отправляем запрос
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# записываем данные сайта в html-файл
# with open("index.html", "w", encoding='utf-8') as file:
#     file.write(src)

# считываем данные
# with open("index.html", encoding='utf-8') as file:
#     src = file.read()

# обрабатываем данные
# soup = BeautifulSoup(src, "lxml")
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href") # находим все ссылки на категории продуктов

# создаем словарь с категориями и заполняем его именами категорий+ссылка
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")

#     all_categories_dict[item_text] = item_href

# записываем словарь в json-файл
# with open("all_categories_dict.json", "w", encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# считываем данные из json-файла
with open("all_categories_dict.json", encoding='utf-8') as file:
    all_categories = json.load(file)

# сколько всего итераций и счетчик
iteration_count = int(len(all_categories)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")

# категория и ссылка 
for category_name, category_href in all_categories.items():

    # заменяем неудобные символы
    # rep = [",", " ", "-", "'"]
    # for item in rep:
    #     if item in category_name:
    #         category_name = category_name.replace(item, "_")

    # отправляем запрос по ссылке на категорию
    # req = requests.get(url=category_href, headers=headers)
    # src = req.text

    # записываем данные со страницы
    with open(f"data/{count}_{category_name}.html", "w", encoding='utf-8') as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # собираем заголовки таблицы
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    # записываем данные в csv-таблицу
    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

    # собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []
    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        # добавляем данные продуктов в таблицу
        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
    
    # записыем данные продуктов категории в json-файл
    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Итерация {count}. {category_name} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось итераций: {iteration_count}")
    sleep(random.randrange(2, 4))