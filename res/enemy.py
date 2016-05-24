from . import entity

class Enemy(entity.Entity):
    def __init__(self):
        super().__init__()
        self.hostile = True
        self.weapon = None
        self.armour = None

    def attack_player(self, player):
        player.HP -= self.weapon.damage
        return self.weapon.damage
    

class Orc(Enemy):
    def __init__(self):
        super().__init__()
