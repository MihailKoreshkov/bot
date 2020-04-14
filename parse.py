import requests
from bs4 import BeautifulSoup4


url = 'http://dmik.ru/'
HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
           'Accept':
           '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def create_bsObj(html_page):
    soup = BeautifulSoup(html_page.text, 'html.parser')
    return soup


def parse_films_name(bsObj):
    data = bsObj.find_all('a', class_='name')
    films_name = []
    for name in data:
        films_name.append(name.get_text())
    return films_name

def parse_films_description(bsObj, qua_films: int): 
    data = bsObj.find_all('p', class_='')            
    films_description = []
    counter = 0
    while qua_films != counter:
        films_description.append(data[counter].get_text())
        counter += 1
    return films_description    

def parse_date_films(bsObj):
    data = bsObj.find_all('a', class_='date')
    films_date = []
    for date in data:
        films_date.append(date.get_text())
    return films_date


