class partnership : 
    def __init__(self, name, description, inscription_date):
        self.name = name
        self.description = description
        self.inscription_date = inscription_date
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_inscription_date(self):
        return self.inscription_date
    
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description
    
    def set_inscription_date(self, inscription_date):
        self.inscription_date = inscription_date
