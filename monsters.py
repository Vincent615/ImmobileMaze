class Lv1_fodder():
    """Fodder monster with attributions"""
    def __init__(self):
        self.descript = 'A cannon folder said no words'
        self.name = "Lv1 Cannon Fodder"
        self.hp = 20
        self.damage = 5
        self.resistance = 1

class Lv2_fodder():
    """Fodder monster with attributions"""
    def __init__(self):
        self.descript = 'A cannon folder said no words'
        self.name = "Lv2 Cannon Fodder"
        self.hp = 30
        self.damage = 5
        self.resistance = 2

dragon_descript = '''Owner of the Dungeon,
    \tFirst boss of the journal:\n\n\t\tBlazing Dragon!!!'''

class Dragon():
    """Dragon monster with attributions"""
    def __init__(self):
        self.descript = dragon_descript
        self.name = "Dragon"
        self.hp = 50
        self.damage = 25
        self.resistance = 8

yaranzo_descript = '''The one born from human\'s greeds
    \n\t\tYaranzo!!!'''

class Yaranzo():
    """Yaranzo monster with attributions"""
    def __init__(self):
        self.descript = yaranzo_descript
        self.name = "Yaranzo"
        self.hp = 60
        self.damage = 30
        self.resistance = 10

slime_descript = '''Owner of the Forest,
    \tFinal boss of the journal:\n\n\t\tLittle Slime!!!'''

class Slime():
    """Slime monster with attributions"""
    def __init__(self):
        self.descript = slime_descript
        self.name = "Slime"
        self.hp = 5
        self.damage = 50
        self.resistance = 50
