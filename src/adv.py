from room import Room
from player import Player
from item import  Items


# Declare all the items
sword = Items("Broad Sword", "Weapon", 20, 25)
poison = Items("Elixer", "Potion", 40, 2)


# Declare all the rooms

outside = Room("Outside Cave Entrance", "North of you, the cave mouth beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", f"""You've found the long-lost treasure {Items.name}
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")



# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Deadpool', 'outside')
newPlayer.current_location = outside
# Write a loop that:
while True:
	try:
# * Prints the current room name
		print(newPlayer.current_location)
# * Prints the current description (the textwrap module might be useful here).
		print(newPlayer.current_location.description)
# * Waits for user input and decides what to do.
		user_input = input('What do you want to do? [n, s, e, w] ')
# If the user enters a cardinal direction, attempt to move to the room there.
		if user_input in {'n', 's', 'e', 'w'}:

	# if newPlayer.current_location.n_to is not None:
			if hasattr(newPlayer.current_location, f'{user_input}_to'):
				newPlayer.current_location = getattr(newPlayer.current_location, f'{user_input}_to')

# Print an error message if the movement isn't allowed.
	except AttributeError:
		print('Invalid Move')
		break
# 	if getattr(newPlayer.current_location, f'{user_input}_to'):
# 		print('Error: unable to move to that location')
# If the user enters "q", quit the game.
	if user_input == 'q':
		quit()

print(sword.type)
