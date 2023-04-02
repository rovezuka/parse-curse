import re
from bs4 import BeautifulSoup

with open("index_html.html", encoding='utf-8') as file:
    src = file.read()
print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title  # возвращает заголовок html-страницы
print(title)
print(title.text)
print(title.string)

# # .find() .find_all()  # поиск тега/поиск всех тегов по запросу
# page_h1 = soup.find("h1")
# print(page_h1)

# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")  # поиска тега div с указанным классом
# print(user_name.text.strip())

# user_name = soup.find(class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
#     print(item.text)

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)

# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

# # .find_parent() .find_parents()  # поиск снизу вверх - предыдущий попавшийся родитель/все предыдущие родители. Можно указать тег
# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

# # .next_element .previous_element  # следующий и предыдущий тег на странице
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# # .find_next_sibling() .find_previous_sibling()  # следующий и предыдущий блок
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# # .find_next()  # следующий тег
# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text  # комбинирование методов
# print(post_title)

# links = soup.find(class_="some__links").find_all("a")
# print(links)

# for link in links:  # получение атрибутов через метод get и поиска по ключу в словаре
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]

#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]

#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Одежда")  # поиска тега по тексту = не работает
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text="Одежда для взрослых")  # soup нужно полное значение, чтобы найти
# print(find_a_by_text)

# re.compile # решает проблему выше
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))  # ищет теги, у которых текст начинает на Одежда
# print(find_a_by_text)

# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))  # решение проблемы разных регистров, передаем два варианта начала текста в re.compile
# print(find_all_clothes)