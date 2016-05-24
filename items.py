from res.item import Item
from res.weapon import Weapon
from res.armour import Armour

blunt_rock = Weapon("Blunt rock", 0, "A blunt for bashing heads, not as sharp as a sharp rock", 5)
farming_clothes = Armour("Farming Clothes", 0, "A set of farming clothes, more designed for working in the sun than fighting", 5)
gold_coin = Item("Gold Coin", 1, "")
gold_coin.description = "A circle of gold with a {} on the front.".format(gold_coin.value)