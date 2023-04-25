import requests
from bs4 import BeautifulSoup
from proxy_auth import proxies
import json


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.2.806 Yowser/2.5 Safari/537.36'

}

# collect all fests URLs
fests_urls_list = []
for i in range(0, 264, 24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=24%20Jan%202021&to_date=&where%5B%5D=2&where%5B%5D=3&where%5B%5D=4&where%5B%5D=6&where%5B%5D=7&where%5B%5D=8&where%5B%5D=9&where%5B%5D=10&maxprice=500&o={i}&bannertitle=May"
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w", encoding='utf-8') as file:
        file.write(html_response)

    with open(f"data/index_{i}.html", 'r', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all("a", class_="card-details-link")

    for item in cards:
        fest_url = "https://www.skiddle.com" + item.get("href")
        fests_urls_list.append(fest_url)

# collect fest info
count = 0
fest_list_result = []
for url in fests_urls_list:
    count += 1
    print(count)
    print(url)

    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, "lxml")
        fest_info_block = soup.find(class_ = 'MuiBox-root css-8tc97e').find("div", class_="MuiContainer-root MuiContainer-maxWidthFalse css-1krljt2")
        fest_name = fest_info_block.find("h1").text.strip()
        soup = BeautifulSoup(req.text, "lxml")
        fest_info_block = soup.find(class_ = 'MuiContainer-root MuiContainer-maxWidthLg css-zd1mrw')
        fest_date_tags = fest_info_block.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').find_all('span')
        fest_date = ''
        for elem in fest_date_tags:
            fest_date += elem.text
        fest_location = fest_info_block.find('div', class_='MuiGrid-root MuiGrid-container css-1d3bbye').find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text.strip()
        fest_list_result.append(
            {
                "Fest name": fest_name,
                "Fest date": fest_date,
                "Fest location": fest_location
            }
        )

    except Exception as ex:
        print(ex)
        print("Damn...There was some error...")

with open("fest_list_result.json", "a", encoding="utf-8") as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)