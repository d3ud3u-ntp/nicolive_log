#coding: utf-8

import requests
from bs4 import BeautifulSoup
import time

def get_url(url):
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    next_page = soup.find('div', {'class': 'nextPage'})
    link = next_page.find('a').get('href')
    print(link)
    return link

def put_character(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # div.article-body-inner->div->img src 画像
    body_inner = soup.find('div', {'class': 'article-body-inner'})
    img = body_inner.find('img').get('src')
    # print(img)
    # div.article-body-inner->div->img alt 画像内文字
    alt = body_inner.find('img').get('alt')
    # print(alt)
    # div.article-category->a->text キャラ名
    category = soup.find('div', {'class': 'article-category'})
    character = category.find('a').get_text()

    man_data = img + "," + alt + "," + character + "\n"
    print(man_data)

    with open("misawadata.csv", "a", encoding='utf-8', newline='\n') as f:
        f.write(man_data)


url = "http://blog.livedoor.jp/jigokuno_misawa/eid_69773305.html"

for i in range(100):
    put_character(url)
    time.sleep(1)
    url = get_url(url)
    time.sleep(1)
