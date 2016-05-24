from . import item

class Armour(item.Item):
    def __init__(self, name, value, description, protection):
        super().__init__(name, value, description)
        self.protection = protection
