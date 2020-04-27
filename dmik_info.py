import dmik_db
from datetime import datetime

class Dmik_info:

    def __init__(self):
        pass

    def films_today(self):
        date = datetime.strftime(datetime.now(), '%d')
        films = dmik_db.fetch_to_day(date, "dmik_day_info")
        if len(films) == 2:
            if films[0][0] > films[1][0]:
                print(films[0][2])
            else:
                print(films[1][2])
        else:
            print(films[0][2])

        
      

    def all_films(self):
        films = dmik_db.fetch_all_day("dmik_info")
        for i in range(len(films)):
            print("Название :", films[i][0],'\n',
                "Дата :", films[i][1],"\n",
                "Описание :", films[i][2])
        


