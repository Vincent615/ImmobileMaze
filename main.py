# Course: CS 30
# Period: 2
# Date created: 20/11/23
# Date last modified: 20/11/30
# Name: Yingwen Liu
# Description: A RPG simple menu while encountering a monster


# Set active True
active = True

while active:
    hp = 100    # Player's health points
    hp_slime = 1    # Slime's health points
    attack = ['attack', 'a']   # Command list for attacking
    heal = ['heal', 'h']   # Command list for healing
    escape = ['escape', 'e']   # Command list for escaping
    backpack = ['bagpack', 'pack', 'b']   # Command list for backpack
    quit = ['quit', 'q']    # # Command list to quit the game

    # Show the boss player encountering
    print('''\n>>> Boss encountering <<<\n\n\tOwner of the Forest,
    \tFinal boss of the journal:\n\n\t\tLittle Slime!!!''')

    # Keep the loop running if hp is greater than zero
    while hp > 0:
        # Let the player choose one of the actions
        print('\nYou can choose one of the following actions:')
        print('* Attack (A)\n* Heal (H)\n* Escape (E)')

        action = '* Backpack (B)\n* Quit (Q)\n>>> '
        action = input(action).lower()   # Replace the input into lower form

        if action in attack:
            hp = hp - 30    # hp minus 30
            # Show the status of Slime and player
            print(f'\n- The Slime missed your attack.\n  Hp left: {hp_slime}')
            print(f'- You got one crit hit from the Slime.\n  Hp left: {hp}')

        elif action in heal:
            # Ask player to buy food or not
            print('\n- There is no food in your backpack.')
            print('\nWould you like to buy some from the market?')
            buy = input('* Yes\n* No\n>>> ')
            buy = buy.lower()   # Replace the input into lower form
            if buy == 'yes':
                # Tell player that the action is unavailable
                print('\n- Sorry, you don\'t have enough coins')
            else:
                # Contunue the loop
                continue

        elif action in escape:
            hp = hp - 20    # hp minus 20
            # Show the status of player
            print('\n- You failed to escape.')
            print(f'  You got one hit from the Slime.\n- Hp left: {hp}')

        elif action in backpack:
            # Print the messages of backpack
            print(f'\nCurrent Hp:\t{hp}')
            print('Main Weapon:\n* Diamond Sword, Sharpness III')
            print('Secondary Weapon:\n* Iron Sheld, Protect II')
            print('Armor:\n* Diamond Armor, Protect II\nFoods:\n* None')
            # Ask player back to fight
            input('\n- Press Enter back to the fight.\n>>> ')

        elif action in quit:
            # Break the loop and stop the game
            active = False
            break

        else:
            # Print a message for unexpected command
            print('\n- Invalid command.')

    # Print a message if hp is less than 0
    print('\n\n\t\t\t_____   _____   _____   _____')
    print('\t|\t   |\t | |\t   |\t   |\t \\')
    print('\t|\t   |\t | |_____  |_____  |_____/')
    print('\t|\t   |\t |\t\t | |\t   |\___')
    print('\t|_____ |_____|  _____| |_____  |\t\_')
    print('\n\n\t\t\t  >>> Game Over <<<\n\n')

    # Ask player to play again if killed by Slime
    if active:
        input('\n- Press Enter to play again.\n>>> ')
