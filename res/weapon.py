from . import item

class Weapon(item.Item):
    def __init__(self, name, value, description, damage):
        super().__init__(name, value, description)
        self.damage = damage
