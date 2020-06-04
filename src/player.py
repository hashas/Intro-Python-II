# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room

	def move_to(self, direction, current_location):
		# try to move in the specified direction
		attribute = direction + '_to'

		# if we can move in specified direction from our current location/room
		# if 'current_location' has 'attribute' then we can move in that direction
		# if it doesn't, then its not possible to move in the specified direction from this room
		if hasattr(current_location, attribute):
			# return the room in the above specified direction
			return getattr(current_location, attribute)

		# if we can't go that way
		print("You can't go that way\n")
		return current_location