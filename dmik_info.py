import dmik_db

class Dmik_info:

    def __init__(self):
        pass

    def films_today(self):
        pass

    def all_films(self):
        films = dmik_db.fetch_all_day("dmik_info")
        for i in range(len(films)):
            print("Название :", films[i][0],'\n',
                "Дата :", films[i][1],"\n",
                "Описание :", films[i][2])
        



