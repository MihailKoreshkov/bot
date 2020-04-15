import requests
from bs4 import BeautifulSoup4


class Parser_dmik:
    
    HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
           'Accept':
           '*/*'}

    def __init__(self):
        self._html = self._get_html()
        self._bsObj = self._create_bsObj()


    def _get_html(self, url='http://dmik.ru/'):
        r = requests.get(url, headers=HEADERS, params=params)
        return r


    def _create_bsObj(self, html_page):
        soup = BeautifulSoup(html_page.text, 'html.parser')
        return soup


    def parse_data(self, bsObj, tag: str, class_: str, quality_iter=None) -> list:
        parse_obj = bsObj.find_all('{}', class_="{}").format(tag, class_)
        data = []
        if quality_iter:
            counter = 0
            while quality_iter != counter:
                data.append(parse_obj[counter].get_text())
                counter += 1
        else:
            for i in parse_obj:
                data.append(date.get_text())
    
        return data
