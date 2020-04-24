import dmik_db
frm datetime import datetime

class Dmik_info:

    def __init__(self):
        pass

    def films_today(self):
        date = datetime.strftime(datetime.now(), '%d')
        films = dmik_db.fetch_to_day(date, "dmik_day_info")
        # надо добавить в метод Parser_dmik.get_dmik_films_to_day из <td id="CalendTD26" class="t0"><a class="typ2" title="">24</a></td>
        # забрать число из айди календ и добавить его третим значением в таблицу dmik_day_info
      

    def all_films(self):
        films = dmik_db.fetch_all_day("dmik_info")
        for i in range(len(films)):
            print("Название :", films[i][0],'\n',
                "Дата :", films[i][1],"\n",
                "Описание :", films[i][2])
        



