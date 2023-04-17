'''Шаг 1: Собрать все ссылки на каждого пользователя
и записать их в отдельный файл'''
'''Шаг 2: Пройтись по каждой ссылке и забрать имя, партию, ссылки на соц.сети(если есть)'''
import requests
from bs4 import BeautifulSoup
import json

# links = []
# for i in range(0, 760, 20):
#         url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={i}'
#         person_page = requests.get(url).content
#         soup = BeautifulSoup(person_page, 'lxml')
#         tags = soup.find_all('a')
#         for tag in tags:
#                 link = tag.get('href')
#                 links.append(link)
# with open('links.txt', 'a') as file:
#         for link in links:
#                 file.write(f'{link}\n')
        
with open('links.txt', encoding='utf-8') as file:
    data_dict = []
    person_page = [link.strip() for link in file.readlines()]
    count = 0
    for i in person_page:
        url = i
        person_text = requests.get(url).content
        person_soup = BeautifulSoup(person_text, 'lxml')
        person_info = person_soup.find(class_='col-xs-8 col-md-9 bt-biografie-name').find('h3').text
        name, party = person_info.strip().split(',')
        data = {
            'person_name': name.strip(),
            'person_party': party.strip()
        }
        data_dict.append(data)
        with open('data.json', 'w', encoding='utf-8') as data_json:
            json.dump(data_dict, data_json ,indent=4)
        count += 1
        print(f'#{count}: {i} is done!')
        

