# Course: CS 30
# Period: 2
# Date created: 20/11/23
# Date last modified: 20/12/20
# Name: Yingwen Liu
# Description: A RPG simple menu while encountering a monster


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
    # Show the game background
    print('You woke up.\nYou find you are in a abandoned dungeon.')
    print('\n- The goal is to >>> Stay Alive <<<')
    safe(0)


def attacking(Monster):
    if Player.damage < Monster.resistance:
        Monster.hp =- 1
        return
    else:
        Monster.hp = Monster.hp + Monster.resistance - Player.damage
        return
    # Show the status of the monster and player
    print(f'\n- You attacked {Monster.name}.\n  Hp left: {Monster.hp}')
    if Monster.damage < Player.resistance:
        Player.hp =- 1
        return
    else:
        Player.hp = Player.hp + Player.resistance - Monster.damage
        return
    print(f'- You got one hit from the {Monster.name}.')


def healing():
    if len(Backpack.bandages) == 0:
        print('\n- There is no bandage in your backpack.')

    else:
        print(f'Available bandages: {len(Backpack.bandages)}')
        a = input('How many will be used? Each one + 10 hp\n>>> ')
        if int(a) <= len(Backpack.bandages):
            Player.hp =+ int(a) * 10
            Backpack.bandages.remove(0)
            return
        else:
            print('\n- There are not enough bandages.')


def escaping(Monster):
    escapable = random.randint(0, 4)
    if escapable == 1:
        print('\n- You failed to escape.')
        print(f'  You got one hit from the {Monster.name}.')
        Player.hp = Player.hp + Player.resistance - Monster.damage
        return
    else:
        print('\n- You escaped successfully.')
        safe()


def moving(round):
    lottery = random.randint(1, 5)
    if lottery == 1:
        print('\n- Nothing happened.')
    elif lottery > 2:
        danger(round)
    else:
        while True:
            print('\n- You find a chest.\n\nDo you want to open it?')
            action = '* Open\n* Leave\n>>> '
            action = input(action).lower()   # Replace the input into lower form
            if action == 'open':
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
    while True:
        print('\nYou can choose one of the following actions:')
        print('* Front (F)\n* Left (L)\n* Right (R)')
        action = '* Backpack (B)\n* Quit (Q)\n>>> '
        action = input(action).lower()   # Replace the input into lower form
        if action in backpack:
            backpacking()

        elif action in quit:
            # Break the loop and stop the game
            lost()
            break

        elif action in move:
            moving(round)
        else:
            # Print a message for unexpected command
            print('\n- Invalid command.')


def danger(round):
    while Player.hp > 0:
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
            action = input(action).lower()   # Replace the input into lower form

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
            if round != 10:
                print(f'You sucessfully killed the {Monster.name}')
                round = round + 1
                safe(round)

            elif round == 10:
                print('- You found a mega legendary chest.')
                print('Do you want to open it?')
                action = input('* Yes\n* No\n>>> ')
                action = input(action).lower()   # Replace the input into lower form
                if action == 'yes':
                    continue
                elif action == 'no':
                    round = round + 1
    else:
        lost()


def lost():
    # Print a message if the player lost the game
    print('\n\n\t\t\t_____   _____   _____')
    print('\t|\t   |\t | |\t\t  |')
    print('\t|\t   |\t | |_____\t  |')
    print('\t|\t   |\t |\t\t |\t  |')
    print('\t|_____ |_____|  _____|\t  |')
    print('\n\n\t\t\t  >>> Game Over <<<\n\n')
