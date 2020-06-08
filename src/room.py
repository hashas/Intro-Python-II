# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self,  name, subtext):
		self.name = name
		self.subtext = subtext
		self.items = []

	def __str__(self):
		return f"{self.name}"

	def print_description(self):
		return f"{self.subtext}"

	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		for i in self.items:
			if item == i.name:
				self.items.remove(i)


	# testing:
	def print_items(self):
		message = "Items in this room: "
		for item in self.items:
			message += f"{item.__str__()}\n"
		return message
    # def print_items(self):
    #     message = "Items in this room: "

    #     for item in self.items:
    #         message += f"{item.__str__()}\n"