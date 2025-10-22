import rand_utils

hats = [Hats.Brown_Hat, Hats.Cactus_Hat,
		Hats.Carrot_Hat,
		Hats.Gold_Hat, Hats.Gray_Hat,
		Hats.Green_Hat, Hats.Purple_Hat,
		Hats.Straw_Hat, Hats.Sunflower_Hat,
		Hats.Traffic_Cone, Hats.Tree_Hat,
		Hats.Wizard_Hat]
		
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

def for_all_row(f):
	def row():
		change_hat(rand_utils.random_elem(hats))
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

def for_all_col(f):
	def col():
		change_hat(rand_utils.random_elem(hats))
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(col):
			col()
		move(East)