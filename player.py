class Player():
    def __init__(self):
        """Player with attributions"""
        self.hp = 100
        self.damage = 20000
        self.resistance = 1000000


class Backpack():
    def __init__(self):
        """Items in the backpack"""
        self.bandages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.weapon = ['Diamond sword']
        self.armor = ['Armor']
