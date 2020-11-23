# Course: CS 30
# Period: 2
# Date created: 20/11/19
# Date last modified: 20/11/22
# Name: Yingwen Liu
# Description: Three dictionaries about characters, inventories and locations


# Create a dictionary of characters in the RPG
characters = {
    # Describe the Player and its attributes through a dictionary
    'brave (player)': {
        'description': 'a guy who\'s risking in a dungeon for treasure',
        'health': 100,
        'damage': 5,
        'resistance': 0,
        },
    # Describe the Dragon and its attributes through a dictionary
    'dragon': {
        'description': 'the first boss and the owner of the dungeon',
        'health': 50,
        'damage': 25,
        'resistance': 8,
        },
    # Describe the Yaranzo and its attributes through a dictionary
    'yaranzo': {
        'descrption': 'born for human\'s greeds',
        'health': 80,
        'damage': 30,
        'resistance': 10,
        },
    # Decribe the Slime and its attributes through a dictionary
    'slime': {
        'description': 'the owner of the forest',
        'health': 10,
        'damage': 50,
        'resistance': 50,
        },
    }

# Loop the dictionary, characters and print its keys
for character, traits in characters.items():
    print(f'*The {character.title()}')    # Print the keys
    # Loop the dictionary traits and print its items
    for attribute, descript in traits.items():
        print(f'\t{attribute.title()}: {descript}')
    print()   # Print an extra blank line after each loop

print()   # Print an extra blank line after the loop


# Create a dictionary of the locations in the RPG
locations = {
    # Describe the Dungeon with a list
    'dungeon': [
        'spawn point of the world',
        'place for player to level up',
        ],
    # Describe the Treasure Palace with a list
    'treasure palace': [
        'nest of the dragon',
        'hidden place for the yaranzo',
        ],
    # Describe the Forest with a list
    'forest': [
        'world outside the dungeon',
        'home of the final boss',
        ],
    }

# Loop the dictionary, locations and print its keps and values seperately
for locate, descript in locations.items():
    print(f'{locate.title()}\n\tis the {descript[0]} and the {descript[1]}.')

print('\n\n')   # Print 2 blank lines after the loop


# Create a dictionary of the inventory in the RPG
inventory = {
    # Create a dictionary about weapons in inventory's key
    'weapons': {
        # Describe the Wooden Sword through a dictionary
        'wooden sword': {
            'description': 'a great weapon for a newbie',
            'damage': 5,
            'resistance': 0,
            'available enchances': [
                'sharpness I',
                'sharpness II',
                'sharpness III',
                ],   # A list of available enchances
            },
        # Describe the Iron sword through a dictionary
        'iron sword': {
            'description': 'a great weapon for a pro',
            'damage': 10,
            'resistance': 0,
            'available enchances': [
                'sharpness I',
                'sharpness II',
                'sharpness III',
                ],   # A list of available enchances
            },
        # Describe the Diamond Sword through a dictionary
        'diamond sword': {
            'description': 'a great weapon for an expert',
            'damage': 15,
            'resistance': 0,
            'available enchances': [
                'sharpness I',
                'sharpness II',
                'sharpness III',
                ],   # A list of available enchances
            },
        # Describe the Wooden Sheld through a dictionary
        'wooden sheld': {
            'description': 'a great secondary weapon for a pro',
            'damage': 1,
            'resistance': 3,
            },
        # Describe the Iron Sheld through a dictionary
        'iron sheld': {
            'description': 'a great secondary weapon for an expert',
            'damage': 3,
            'resistance': 5,
            },
        # Describe the Bow through a dictionary
        'bow': {
            'description': 'a great weapon for leaving in backpact',
            'damage': 12,
            'resistance': 0,
            'available enchance': ['power V'],   # List of available enchance
            },
        },
    # Create a dictionary about gears in inventory's key
    'gears': {
        # Describe the Iron Armor through a dictionary
        '*iron armor': {
            'description': 'a great suit of gears for a pro',
            'resistance': 3,
            'available enchances': [
                'protect I',
                'protect II'
                ],    # A list of available enchances
            },
        # Describe the Diamond Armor through a dictionary
        'diamond armor': {
            'description': 'a great suit of gears for an expert',
            'resistance': 8,
            'available enchances': [
                'protect I',
                'protect II'
                ],    # A list of available enchances
            },
        },
    # Create a dictionary about foods in inventory's key
    'foods': {
        # Describe the Apple through a dictionary
        '*apple': {
            'description': 'an apple a day keeps a doctor away',
            'healing points': 5,
            },
        # Describe the Golden Apple through a dictionary
        '*golden apple': {
            'description': 'isn\'t this eatable?',
            'healing points': 15,
            'available ehchance': ['echanced']     # List of available enchance
            },
        # Describe the Enchanced Golden Apple through a dictionary
        '*enchanced golden apple': {
            'description': 'is this eatable?',
            'healing points': 30,
            },
        # Describe the Enchanced Golden Apple through a dictionary
        '*tolem': {
            'description': 'used for resurrection',
            'healing points': 100,
            }
        }
    }

# Loop the dictionary, inventory and print its keys
for type, descriptions in inventory.items():
    print(f'{type.title()}:')
    # Loop the dictionary descriptions and print its keys
    for item, descripts in descriptions.items():
        print(f'{item.title()}')
        # Loop the dictionary descripts and print its items
        for attribute, descript in descripts.items():
            print(f'\t{attribute.title()}: {descript}')
        print()   # Print a blank line after each loop
    print()   # Print a blank line after each loop
