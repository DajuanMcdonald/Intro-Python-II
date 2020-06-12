class Items:
	def __init__(self, name, type, attack, protect):
		self.name = name
		self.type = type
		self.attack = int(attack)
		self.protect = int(protect)


	def on_take(self):
		print(f'You picked up a {self.type} : {self.name}')
		print(f'It has attack ability of {self.attack}')
		print(f'with a protect ability of {self.protect}')

	def on_drop(self):
		print(f'You dropped an item {self.name}')
