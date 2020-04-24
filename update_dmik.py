from parser_dmik import Parser_dmik
import dmik_db



class Update_dmik:
  
    def __init__(self):
        self.delete_data()
        self.anons = Parser_dmik().get_dmik_anons()
        self.films_to_day = Parser_dmik().get_dmik_films_to_day()
        self.add_to_base()
  

    def add_to_base(self):
        dmik_db.insert("dmik_info", self.anons)
        dmik_db.insert("dmik_day_info",self.films_to_day)


    def delete_data(self):
        dmik_db.delete("dmik_info")
        dmik_db.delete("dmik_day_info")


Update_dmik()
