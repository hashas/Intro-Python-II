from room import Room
# import player
from player import Player
# import textwrap
import textwrap
# import item
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# this specifies new attributes i.e. "n_to" and assigning them to certain properties 
# on the 'rooom' object

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms
torch = Item("Torch", "Lights the way")
shield = Item("Shield", "A creaky wooden shield")
sword = Item("Rusty Sword", "Not sure how many whacks I'll get out of this")
coin = Item("Bitcoin", "This might be worth a lot!")

# Link rooms to items (I need an addItem method in Room class)
room['outside'].add_item(torch)
room['outside'].add_item(shield)
room['overlook'].add_item(sword)
room['treasure'].add_item(coin)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Hasan", room["outside"])
print(f"Welcome, {player.name}")

# Write a loop that:
game_over = False

# helper function to skip input we don't understand
def skip_input():
	print("I don't understand that")

# helper function to print all available commands
def print_help_text():
	print("""
    Valid commands:
        -[n]: move north
        -[s]: move south
        -[e]: move east
        -[w]: move west
        -[q]: quit
        -[help]: help text
    """)

# write a loop that:
while not game_over:
	#
	# * Prints the current room name
	print(player.current_room)
	# * Prints the current description (the textwrap module might be useful here).
	# textwrap returns a long string into several lines of max width
	for line in textwrap.wrap(player.current_room.print_description()):
		print(line)
	print("\n")
	for line in textwrap.wrap(player.current_room.print_items()):
		print(line)

	# print items in current room
	# print("Items in this room: ")
	# for item in player.current_room.items:
	# 	print(f"{item}")
	print("\n")

	# * Waits for user input and decides what to do.
    # .strip() w/o any arg removes the leading and trailing white space	
	command = input("What do you want to do? ").strip()

	# check that the command is properly formatted
    # if the input is less than 1 word, call skip_input() function which prints error message
	if len(command) < 1:
		skip_input()
		continue

	# if the command received one word
    # .split() w/o args splits the string at each white space into string of single-words
	if len(command.split()) == 1:

		if command[0] in ['n', 's', 'e', 'w']:
			# use the command to determine next move
			player.current_room = player.move_to(command, player.current_room)
			continue # go to the next loop
		#
		# If the user enters a cardinal direction, attempt to move to the room there.
		# Print an error message if the movement isn't allowed.
		#
		# If the user enters "q", quit the game.
		# if command == "q" or command == "quit":
		elif command[0] in ['q', 'quit', 'exit']:
			game_over = True

		# question mark command that prints all the commands
		elif command[0] in ['?', 'help']:
			print_help_text()
			continue

		else:
			skip_input()
			continue

	# if the command received two words, handle 'verb' and 'object'
	elif len(command.split()) >= 2:
		verb = command.split()[0]
		# joins the remaining words into single string representing item name
		# in case it is two words
		obj = " ".join(command.split()[1:])
		# print(verb)
		# print(type(obj))
		if verb in ['get', 'take']:
			for item in player.current_room.items:
				if obj == item.name:
					# player.current_room.remove_item(obj)
					player.pickup_item(obj)
			player.display_backpack()
		# else:
		# 	print("error")

		if verb in ['drop']:
			for item in player.inventory:
				if obj == item:
					player.drop_item(obj)
					# 'obj' here is a str, but we need to add an Item object to 
					# 'items' list in current_room
					player.current_room.add_item()
			player.display_backpack()

	else:
		skip_input()
		continue