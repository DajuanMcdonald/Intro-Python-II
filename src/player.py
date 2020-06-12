# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

	def __init__(self, name, current_location, inventory):
		self.name = name
		self.current_location = current_location
		self.inventory = inventory

	def move(self, direction):
		next_room = getattr(self.current_location, f'{direction}_to')
		if next_room is not None:
			self.current_location = next_room
			print(f'You are in {self.current_location}')
		else:
			print(f'Cannot move there, it is a dead end, {self.name}')