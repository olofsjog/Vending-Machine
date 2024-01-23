import math
import sqlite3

print("\n\n\n\n\n\n\n\n\n\nVENDING MACHINE")
print("-----------------")
print("[Q] for Quit")
print("[W] for Up")
print("[S] for Down")
print("[B] for Back")
print("[M] for Menu")
print("[C] for Cart")
print("[I] for Inventory")
print("-----------------")
menu = input("INPUT ANYTHING: ")

print("\n\n\n\n\n\n\n\n\n\n")
print("")

#account & previous balance & inventory
#currency
#add balance

#vending machine menu [OPEN]

#####################################CATEGORY#####################################

category = ["soda", "chips", "candy"]
pointer = category[0]
menu_option = 0
move_pointer = ''
soda_pointer = ''
chips_pointer = ''
candy_pointer = ''
loop1 = True

while loop1:

    if str.lower(move_pointer) == "w" or str.lower(move_pointer) == "s":
        if str.lower(move_pointer) == "w":
            if menu_option == 0:
                menu_option = menu_option+2
            elif menu_option != 0:
                menu_option = menu_option-1

        elif str.lower(move_pointer) == "s":
            if menu_option == 2:
                menu_option = menu_option-2
            elif menu_option != 2:
                menu_option = menu_option+1

        else:
            menu_option = 0

    elif str.lower(move_pointer) == "b":
        loop1 = False

    elif str.lower(move_pointer) == "m":
        loop1 = False
        loop2 = False

    elif move_pointer == '':
        move_pointer = move_pointer
        menu_option = 0

    elif str.lower(move_pointer) == "q":
        quit()

    else:
        quit()

    pointer = category[menu_option]

    if pointer == "soda":
        soda_pointer = '<'
        chips_pointer = ''
        candy_pointer = ''

    elif pointer == "chips":
        soda_pointer = ''
        chips_pointer = '<'
        candy_pointer = ''

    elif pointer == "candy":
        soda_pointer = ''
        chips_pointer = ''
        candy_pointer = '<'

    print("\n\n\n\n\n\n\n\n\n\nVENDING MACHINE")
    print("---------------")
    print(f"1. SODA {soda_pointer}")
    print(f"2. CHIPS {chips_pointer}")
    print(f"3. CANDY {candy_pointer}")
    print("---------------")

    try:
        move_pointer = input("INPUT: ")
        move_pointer = str(move_pointer)
    except ValueError:
        print("Invalid Input")
        continue

#####################################ITEMS#####################################
    
    try:
        if move_pointer == '':
            item = ["", "", ""]
            menu_option = 0
            move_pointer = ''
            one_pointer = ''
            two_pointer = ''
            three_pointer = ''
            loop2 = True

            while loop2:

                if str.lower(move_pointer) == "w" or str.lower(move_pointer) == "s":
                    if str.lower(move_pointer) == "w":
                        if menu_option == 0:
                            menu_option = menu_option+2
                        elif menu_option != 0:
                            menu_option = menu_option-1

                    elif str.lower(move_pointer) == "s":
                        if menu_option == 2:
                            menu_option = menu_option-2
                        elif menu_option != 2:
                            menu_option = menu_option+1

                    else:
                        menu_option = 0

                elif str.lower(move_pointer) == "b":
                    loop2 = False

                elif str.lower(move_pointer) == "m":
                    loop1 = False
                    loop2 = False

                elif move_pointer == '':
                    move_pointer = move_pointer
                    menu_option = 0

                elif str.lower(move_pointer) == "q":
                    quit()

                else:
                    quit()

                if pointer == "soda":
                    item = ["COLA", "FANTA", "SPRITE"]
                    pointer2 = item[menu_option]

                    if pointer2 == "COLA":
                        one_pointer = '<'
                        two_pointer = ''
                        three_pointer = ''

                    elif pointer2 == "FANTA":
                        one_pointer = ''
                        two_pointer = '<'
                        three_pointer = ''

                    elif pointer2 == "SPRITE":
                        one_pointer = ''
                        two_pointer = ''
                        three_pointer = '<'

                elif pointer == "chips":
                    item = ["SALTED", "GRILL", "DILL"]
                    pointer2 = item[menu_option]

                    if pointer2 == "SALTED":
                        one_pointer = '<'
                        two_pointer = ''
                        three_pointer = ''

                    elif pointer2 == "GRILL":
                        one_pointer = ''
                        two_pointer = '<'
                        three_pointer = ''

                    elif pointer2 == "DILL":
                        one_pointer = ''
                        two_pointer = ''
                        three_pointer = '<'

                elif pointer == "candy":
                    item = ["HARIBO", "MARABOU", "DAIM"]
                    pointer2 = item[menu_option]

                    if pointer2 == "HARIBO":
                        one_pointer = '<'
                        two_pointer = ''
                        three_pointer = ''

                    elif pointer2 == "MARABOU":
                        one_pointer = ''
                        two_pointer = '<'
                        three_pointer = ''

                    elif pointer2 == "DAIM":
                        one_pointer = ''
                        two_pointer = ''
                        three_pointer = '<'

                print("\n\n\n\n\n\n\n\n\n\nVENDING MACHINE")
                print("---------------")
                print(f"1. {item[0]} {one_pointer}")
                print(f"2. {item[1]} {two_pointer}")
                print(f"3. {item[2]} {three_pointer}")
                print("---------------")

                try:
                    move_pointer = input("INPUT: ")
                    move_pointer = str(move_pointer)
                except ValueError:
                    print("Invalid Input")
                    continue
        else:
            continue

    except ValueError:
        print("Invalid Input")
        continue

#cart
#total cost
#pay

#see inventory