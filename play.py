# Course: CS 30
# Period: 2
# Date created: 20/11/23
# Date last modified: 20/12/20
# Name: Yingwen Liu
# Description: A RPG game talking about the brave risking in the dungeon


from player import Player
from player import Backpack
import monsters as m
import random

attack = ['attack', 'a', '1']   # Command list for attacking
heal = ['heal', 'h', '2']   # Command list for healing
escape = ['escape', 'e', '3']   # Command list for escaping
move = ['front', 'f', '1', 'left', 'l', '2', 'right', 'r', '3']
backpack = ['backpack', 'b', '4']   # Command list for backpack
quit = ['quit', 'q', '5']    # Command list to quit the game


def play():
    '''The beginning of the game'''
    print('You woke up.\nYou find you are in a abandoned dungeon.')
    print('\n- The goal is to >>> Stay Alive <<<')
    safe(0)     # 0 refers to 0 round of the game


def attacking(Monster):
    '''The function shows the cauculation if the player attacked'''
    if Player.damage < Monster.resistance:
        # Monster's hp minus one if its resistance if higher
        Monster.hp = Monster.hp - 1
        return
    else:
        # A formula to calculate damage on the monster
        Monster.hp = Monster.hp + Monster.resistance - Player.damage
        return
    # Show the status of the monster and player
    print(f'\n- You attacked {Monster.name}.\n  Hp left: {Monster.hp}')
    print(f'\n{Monster.name}\'s turn:')

    if Monster.damage < Player.resistance:
        # Player's hp minus one if its resistance if higher
        Player.hp = Player.hp - 1
        return
    else:
        # A formula to calculate damage on the player
        Player.hp = Player.hp + Player.resistance - Monster.damage
        return
    print(f'- You got one hit from the {Monster.name}.')


def healing():
    '''Add health points to the player'''
    if len(Backpack.bandages) == 0:
        # Tell the player there is no bandages
        print('\n- There is no bandage in your backpack.')

    else:
        # Ask the player how many it needs
        print(f'Available bandages: {len(Backpack.bandages)}')
        a = input('How many will be used? Each one + 10 hp\n>>> ')
        if int(a) <= len(Backpack.bandages):
            # Each bandage add 10 hp
            Player.hp = Player.hp + int(a) * 10
            # remove a bandage from the list
            Backpack.bandages.remove(0)
            return
        else:
            # Tell the player it asked for too many bandages
            print('\n- There are not enough bandages.')


def escaping(Monster):
    '''There is 25% chance to escape'''
    escapable = random.randint(0, 4)
    if escapable == 1:
        print('\n- You failed to escape.')
        # Recieve one hit from the monster
        print(f'  You got one hit from the {Monster.name}.')
        Player.hp = Player.hp + Player.resistance - Monster.damage
        return
    else:
        # Tell the player it escaped
        print('\n- You escaped successfully.')
        # Call the function safe()
        safe()


def moving(round):
    lottery = random.randint(1, 5)
    # 20% to get nothing
    if lottery == 1:
        print('\n- Nothing happened.')
    # 60% to encounter a monster
    elif lottery > 2:
        danger(round)
    else:
    # 20% to get a chest
        while True:
            # Ask player to open or not
            print('\n- You find a chest.\n\nDo you want to open it?')
            action = '* Open\n* Leave\n>>> '
            action = input(action).lower()   # Replace into lower form
            if action == 'open':
                # Tell the player there is nothing
                # This will be updated to find some gears
                print('- There is nothing inside')
                break
            elif action == 'leave':
                break
            else:
                # Print a message for unexpected command
                print('\n- Invalid command.')


def backpacking():
    '''Print the messages of backpack'''
    print(f'\nWeapon:\n* {Backpack.weapon}')
    print(f'Armor:\n* {Backpack.armor}')
    print(f'Bandages:\n* {len(Backpack.bandages)}')
    # Ask player back to fight
    input('\n- Press Enter back to the fight.\n>>> ')


def safe(round):
    '''Actions and their results when player is exploring'''
    while True:
        # Ask player to take an action
        print('\nYou can choose one of the following actions:')
        print('* Front (F)\n* Left (L)\n* Right (R)')
        action = '* Backpack (B)\n* Quit (Q)\n>>> '
        action = input(action).lower()   # Replace the input into lower form
        
        if action in backpack:
            # Call the function backpacking
            backpacking()

        elif action in quit:
            # Break the loop and stop the game
            lost()
            break

        elif action in move:
            # Call the function moving
            moving(round)

        else:
            # Print a message for unexpected command
            print('\n- Invalid command.')


def danger(round):
    '''Actions and their results when player encounters a monster'''
    # Run the loop if player's hp is greater than 0
    while Player.hp > 0:
        # Round number and its referance monster
        if round < 10:
            Monster = m.Lv1_fodder()
        elif round == 10:
            Monster = m.Dragon()
        elif round == 11:
            Monster == m.Yaranzo()
        elif 11 < round < 21:
            Monster == m.Lv2_fodder()
        elif round == 21:
            Monster == m.Slime()
        else:
            # Finish the game if the Round is greater than 21
            print('You successfully escape from the forest!')
            print('\n\n\t\t\t  >>> Congratulations <<<\n\n')
            break

        # Show the boss notation if the player encounter a boss
        print('''\n>>> Monster encountering <<<\n''')
        print(f'\n\t{Monster.descript}')
        # Keep the loop running if hp is greater than zero
        if Monster.hp > 0:
            print(f'\n\tCurrent hp:\t{Player.hp}')
            # Let the player choose one of the actions
            print('\nYou can choose one of the following actions:')
            print('* Attack (A)\n* Heal (H)\n* Escape (E)')

            action = '* Backpack (B)\n* Quit (Q)\n>>> '
            action = input(action).lower()   # Replace into lower form
            
            # Actions and their results
            if action in attack:
                attacking(Monster)
            elif action in heal:
                healing()
            elif action in escape:
                escaping(Monster)
            elif action in backpack:
                backpacking()
            elif action in quit:
                # Break the loop and stop the game
                lost()
                break
            else:
                # Print a message for unexpected command
                print('\n- Invalid command.')

        else:
            # Following actions if monster's hp is lower than 0
            if round != 10:
                print(f'You sucessfully killed the {Monster.name}')
                # Add 1 round if the monster is killed
                round = round + 1
                # Call the funciton safe
                safe(round)
            # Following actions if the round number is 10
            elif round == 10:
                # Ask the player to open chest or not
                print('- You found a mega legendary chest.')
                print('Do you want to open it?')
                action = input('* Yes\n* No\n>>> ')
                action = input(action).lower()   # Replace into lower form
                if action == 'yes':
                    # The player will encounter Yaranzo this round
                    continue
                elif action == 'no':
                    # Add 1 more round if the player choose no 
                    round = round + 1
    else:
        # Call the function lost when player's hp is lower than 0
        lost()


def lost():
    # Print a message if the player lost the game
    print('\n\n\t\t\t_____   _____   _____')
    print('\t|\t   |\t | |\t\t  |')
    print('\t|\t   |\t | |_____\t  |')
    print('\t|\t   |\t |\t\t |\t  |')
    print('\t|_____ |_____|  _____|\t  |')
    print('\n\n\t\t\t  >>> Game Over <<<\n\n')
