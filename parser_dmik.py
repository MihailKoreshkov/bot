import requests
import dmik_db
import re
from bs4 import BeautifulSoup



class Parser_dmik:
      
    HEADERS = {'User-Agent':
            'Mozilla/6.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
            'Accept':
            '*/*'}
  
  
    def __init__(self):
        self._bsObj = self._create_bsObj()
  
  
    def _create_bsObj(self, url='http://dmik.ru/'):
        html_page = requests.get(url, headers=self.HEADERS)
        soup = BeautifulSoup(html_page.text, 'html.parser')
        return soup
 

    def parse(self, tag: str, class_=None, quality_iter=None, pattern=None) -> list:
        data = []
        if pattern:
            data = self._bsObj.find_all(tag, class_=pattern)
        else:   
            parse_obj = self._bsObj.find_all(tag, class_=class_)
            if quality_iter:
                counter = 0
                while quality_iter != counter:
                    data.append(parse_obj[counter].get_text())
                    counter += 1
            else:
                for i in parse_obj:
                    data.append(i.get_text())
        return data


    def get_dmik_anons(self):
        title = self.parse('a', 'name')
        date = self.parse('a', 'date')
        description = self.parse('p', len(title))
        sort_data = ()
        data = []
        for i in range(len(title)):
            sort_data = (title[i], date[i], description[i])
            data.append(sort_data)
        return data


    def get_dmik_films_to_day(self):
        pattern = re.compile("typ")
        data = self.parse('a', pattern=pattern)
        sort_data = ()
        day_shedule = []
        for i in range(len(data)):
            sort_data = (data[i].text, data[i].get('title'))
            day_shedule.append(sort_data)
        return day_shedule
        



    
  


    
                 



    





