# dictionary and starting variables
rooms = {
    'Your Room': {'name': 'Your Room', 'first_time': True,
                  'room_description':
                      "You wake to a loud noise. Is it the storm outside?\n"
                      "As you glance at the digital clock next to your bed, it shines 3:00AM in bright red.\n"
                      "Weird. It almost looks… newer?\n"
                      "You shrug it off, close your eyes, and go back to sleep.\n"
                      "\nBANG.\n\n"
                      "It's that sound again. You jump out of bed to go check it out.\n",
                  'south': 'Hallway',
                  'item_command': 'none', 'item_intro': 'none',
                  'item_description': 'Item description goes here.'},
    'Hallway': {'name': 'the Hallway', 'first_time': True,
                'room_description': "It’s dark, but you can still see the outline of "
                                    "three door frames at the end of the hallway.\n"
                                    "The banging definitely came from this direction.\n",
                'north': 'Your Room', 'south': 'Living Room', 'east': 'Bathroom', 'west': 'Storage Room',
                'item_command': 'flashlight', 'item_intro': 'a flashlight',
                'item_description': "As you hold it in your hands, you remember staying up "
                                    "all night reading manga under the bedsheets.\n"
                                    "Your parents always hated it. They were probably right… Right?"},
    'Storage Room': {'name': 'the Storage Room', 'first_time': True,
                     'room_description': "It’s quite basic, but it feels more spacious than you remember.",
                     'east': 'Hallway',
                     'item_command': 'baseball bat', 'item_intro': 'a baseball bat',
                     'item_description': "As you hold it in your hands, you remember using it as a sword growing up.\n"
                                         "You never really liked baseball. You give it one good swing. "
                                         "Yep. Still a great sword."},
    'Bathroom': {'name': 'the Bathroom', 'first_time': True,
                 'room_description': "The moonlight gently bounces off the quartz counter tops "
                                     "and porcelain toilet as you enter.\n"
                                     "Looks like you’re running low on toilet paper.",
                 'west': 'Hallway',
                 'item_command': 'cracked glasses', 'item_intro': 'cracked glasses',
                 'item_description': "As you hold them in your hands, you remember when you first cracked them.\n"
                                     "You were at recess and they flew off your face as you tagged Jimmy Mason.\n"
                                     "Your parents never let you play tag after that."},
    'Living Room': {'name': 'the Living Room', 'first_time': True,
                    'room_description': "As you close the large double-doors behind you, you hear a loud bang again.\n"
                                        "You’re closer to the sound, but you don’t think it’s in this room.",
                    'north': 'Hallway', 'east': 'Kitchen',
                    'item_command': 'manga', 'item_intro': 'a manga',
                    'item_description': "As you hold it in your hands, you remember reading your first manga.\n"
                                        "Took you 10 pages to realize you were reading it backwards.\n"
                                        "You stopped reading manga before you graduated high school. "
                                        "Why’d you ever stop?"},
    'Kitchen': {'name': 'the Kitchen', 'first_time': True,
                'room_description': "You stand on your kitchen’s checker-tiled floors and "
                                    "remember you really need to renovate.\n"
                                    "Suddenly, you hear another loud bang—this time from behind the pantry door.",
                'north': 'Hidden Hallway', 'west': 'Living Room',
                'item_command': 'crumpled note', 'item_intro': 'a crumpled note',
                'item_description': "As you hold it in your hands, you remember leaving secret messages "
                                    "like this all over the house growing up.\n"
                                    "This one says, Remember the hidden hallway. Oh man, how could you forget that!\n"
                                    "You think it’s somewhere in the kitchen."},
    'Hidden Hallway': {'name': 'a Hidden Hallway', 'first_time': True,
                       'room_description': "You haven’t been in here in years. You almost forgot it existed.",
                       'north': '...Your Room?', 'south': 'Kitchen',
                       'item_command': 'report card', 'item_intro': 'a report card',
                       'item_description': "As you hold it in your hands, you remember how you felt when"
                                           " you first read your teacher’s note:\n"
                                           "'Your child spends all their time daydreaming. They’ll never be "
                                           "successful if they don’t start taking life more seriously.'\n"
                                           "Your parents were never more upset."},
    '...Your Room?': {'name': '...Your Room?', 'first_time': True,
                      'room_description': 'Room description goes here.',
                      'south': 'Hidden Hallway',
                      'item_command': 'none', 'item_intro': 'none',
                      'item_description': 'Item description goes here.'}
}
current_room = rooms['Your Room']
directions = ['north', 'south', 'east', 'west']
hidden_player_inventory = ['none']
visible_player_inventory = []
total_items = 0
player_name = ''
player_command = ''
move_command = ''
take_out_command = ''


# function for 'clearing' the screen
def clear_screen():
    print("\n" * 100)


# function for welcome message and setting player name
def welcome():
    print("Welcome to Dreams, a text-based game made by Analog Anthology.")
    print()
    show_instructions()
    print()
    print("---")
    print()
    global player_name
    player_name = input("Enter your name: \n")
    clear_screen()


# function showing the goal of the game and move commands
def show_instructions():
    print("Commands:")
    print(" Move between rooms: go north, go south, go east, go west")
    print(" Pick up items: pick up 'item name'")
    print(" Take out items from inventory: take out 'item name'")
    print(" Quit the game: quit")


# function to display the current statuses
def show_status():
    # location
    if current_room == rooms['Your Room']:
        print()
        print("---")
        pass
    else:
        print()
        print("---")
        print("You are in {}.".format(current_room['name']))

    if (current_room['first_time'] is True) and (current_room['name'] != '...Your Room?'):
        print(current_room['room_description'])
        current_room['first_time'] = False
    else:
        pass

    # available item
    if current_room == rooms['Your Room']:
        print("---")
        print("Your inventory: {}".format(visible_player_inventory))
        print()
    elif current_room == rooms['...Your Room?']:
        print("---")
        print()
    else:
        if current_room['item_command'] in hidden_player_inventory:
            print()
            print("You don't see any useful items here.")
        else:
            print()
            print("You see {}.".format(current_room['item_intro']))
        print("---")
        print("Your inventory: {}".format(visible_player_inventory))
        print()


# function so player can quit the game at any time
def quit_game():
    print()
    print("---")
    print("Thanks for playing!")
    print("---")


def end_game():
    print("Well… you think you’re in your room, but something’s not quite right.\n"
          "Nothing looks how it’s supposed to. It all looks like it did when you were a child.\n"
          "There’s a mirror in the middle of the room. As you look into it you’re young again.\n"
          "There’s still hope in your eyes. And behind you is… you? But you from the future.")
    if total_items == 6:
        print()
        print("As you turn, you embrace yourself and accept the child in you that you repressed for so long.\n"
              "All of a sudden you’re awake. You’re back in your bed and it’s still storming outside.\n"
              "But this time you feel whole.")
        print("YOU WIN.")
    else:
        print()
        print("As you turn, your future self stabs you in the heart.\n"
              "All of a sudden you’re awake. You’re back in your bed and it’s still storming outside.\n"
              "And you still feel empty inside.")
        print("YOU LOOSE.")


# function for core game loop
def main():
    # calling global variables and setting internal ones
    global current_room
    global visible_player_inventory
    global hidden_player_inventory
    global total_items
    global player_command
    global move_command
    global take_out_command

    # welcome players to the game
    welcome()

    # while loop where the primary game loop takes place
    while True:
        # show player's current status
        show_status()

        # check to see if player is in the last room. if yes, then trigger end game content.
        if current_room == rooms['...Your Room?']:
            end_game()
            break
        else:
            # ask user what they'd like to do
            player_command = input("What do you do? (To see a list of commands, type: command). \n").strip().lower()
            move_command = player_command[3:]
            take_out_command = player_command[9:]

            # if statement for player movement
            if move_command in directions:
                if move_command in current_room:
                    clear_screen()
                    current_room = rooms[current_room[move_command]]
                else:
                    # if user attempts to go in unavailable direction
                    clear_screen()
                    print()
                    print("---")
                    print("You can't go that way.")
                    print("---")

            # if statement for player item acquisition
            # TASK: re-word get command to be more clear to players
            elif player_command == 'pick up {}'.format(current_room['item_command']):
                clear_screen()
                print()
                print("---")
                print("You pick up the {}.".format(current_room['item_command']))
                print(current_room['item_description'])
                print("---")
                hidden_player_inventory.append(current_room['item_command'])
                current_room['item_command'] = 'none'
                visible_player_inventory = [x for x in hidden_player_inventory if x != 'none']
                total_items += 1

            # if statement so player can take out items and re-trigger item descriptions
            elif visible_player_inventory.count(take_out_command) == 1:
                clear_screen()
                print()
                print("---")
                print("You take out the {}.".format(take_out_command))
                print(current_room['item_description'])
                print("---")

            # if statement so player print the command list
            elif player_command == 'command':
                clear_screen()
                print()
                print("---")
                show_instructions()
                print("---")

            # if statement so player can quit at anytime
            elif player_command == 'quit':
                quit_game()
                break

            # if user types a command that is not available
            else:
                clear_screen()
                print()
                print("---")
                print("Please enter a valid command.")
                print("---")


# welcome & game function calls
main()
