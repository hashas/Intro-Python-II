from room import Room
# import player
from player import Player
# import textwrap
import textwrap

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
# this specifies new attributes i.e. "n_to" and assings them to certain properties 
# on the 'rooom' object

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Hasan", room["outside"])

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

	# * Waits for user input and decides what to do.
	command = input("What do you want to do? ")

	# check that the command is properly formatted
	if len(command) > 2 or len(command) < 1:
		# print("I don't understand that\n")
		skip_input()
		continue

	if command in ['n', 's', 'e', 'w']:
		# use the command to determine next move
		player.current_room = player.move_to(command, player.current_room)
		continue # go to the next loop
	#
	# If the user enters a cardinal direction, attempt to move to the room there.
	# Print an error message if the movement isn't allowed.
	#
	# If the user enters "q", quit the game.
	# if command == "q" or command == "quit":
	if command in ['q', 'quit', 'exit']:
		game_over = True

	# question mark command that prints all the commands
	if command in ['?', 'help']:
		print_help_text()
		continue

	else:
		skip_input()
		continue