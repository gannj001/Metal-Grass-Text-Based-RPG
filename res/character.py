class Character:
    def __init__(self):
        self.name = ""
        self.location = None
        self.HP = 10
        self.strength = 1
        self.dodge = 1
        self.armour = None
        self.weapon = None
        self.level = 1
        self.inventory = []
        self.title = "Farmer"

    def equip_weapon(self, weapon):
        self.weapon = weapon
        return "You equipped ", weapon.name, "\n"

    def equip_armour(self, armour):
        self.armour = armour
        return "You equipped ", armour.name, "\n"

    def unequip_weapon(self):
        weapon = self.weapon
        self.weapon = None
        self.inventory.append(weapon)
        return "You have unequipped ", weapon.name, "\n"

    def unequip_armour(self):
        armour = self.armour
        self.armour = None
        self.inventory.append(armour)
        return "You have unequipped ", armour.name, "\n"

    def equip_item(self, item):
        status_line = ""
        if type(item) == "Armour":
            if self.armour:
                status_line += self.unequip_armour()
            status_line += self.equip_armour(item)
        elif type(item) == "Weapon":
            if self.weapon:
                status_line += self.unequip_weapon()
            status_line += self.equip_weapon(item)

    def printstatus(self):
        status = """
============- {} -===============
Name:        {}
HP:          {}
Weapon:      {}
Armour:      {}
Location:    {}
Description: {}
""".format((self.name +" the "+ self.title), self.name, self.HP, self.weapon.name, self.armour.name, self.location.name, self.location.description)
        print(status)
