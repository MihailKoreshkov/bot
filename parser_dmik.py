import requests
import dmik_db

from bs4 import BeautifulSoup




class Parser_dmik:
    
    HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
           'Accept':
           '*/*'}


    def __init__(self):
        self._bsObj = self._create_bsObj()


    def _create_bsObj(self, url='http://dmik.ru/'):
        html_page = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        return soup

    def parse_data(self, tag: str, class_: str, quality_iter=None) -> list:
        parse_obj = self._bsObj.find_all(tag, class_=class_)
        data = []
        if quality_iter:
            counter = 0
            while quality_iter != counter:
                data.append(parse_obj[counter].get_text())
                counter += 1
        else:
            for i in parse_obj:
                data.append(i.get_text())

        return data



class Update:

    def __init__(self):
        self.data = self.get_dmik_data()

    def get_dmik_data(self):
        title = Parser_dmik().parse_data('a', 'name')
        date = Parser_dmik().parse_data('a', 'date')
        description = Parser_dmik().parse_data('p', '', len(title))
        sort_data = ()
        data = []
        for i in range(len(title)):
            sort_data = (title[i], date[i], description[i])
            data.append(sort_data)
        return data
        
    def add_to_base(self):
        dmik_db.insert("dmik_info", self.data)
        




