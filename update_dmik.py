from parser_dmik import Parser_dmik
import dmik_db



class Update_dmik:
  
    def __init__(self):
        self.delete_data()
        self.data = Parser_dmik().get_dmik_data()
        self.add_to_base()
  

    def add_to_base(self):
        dmik_db.insert("dmik_info", self.data)


    def delete_data(self):
        dmik_db.delete("dmik_info")


Update_dmik()