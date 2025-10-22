def water(a=0.75):

	a = min(a, 0.75)
	while get_water() <= a:
		use_item(Items.Water)

def move_to(x, y):
	n = get_world_size()
	nowx = get_pos_x()
	nowy = get_pos_y()
	diffx = x - nowx
	abs_diffx = abs(diffx)
	if abs_diffx > n // 2:
		if diffx >= 0:
			diffx = abs_diffx - n
		else:
			diffx = n - abs_diffx
	diffy = y - nowy
	abs_diffy = abs(diffy)
	if abs_diffy > n // 2:
		if diffy >= 0:
			diffy = abs_diffy - n
		else:
			diffy = n - abs_diffy
	if diffx >= 0:
		for _ in range(diffx):
			move(East)
	else:
		for _ in range(-diffx):
			move(West)
	if diffy >= 0:
		for _ in range(diffy):
			move(North)
	else:
		for _ in range(-diffy):
			move(South)

pla = Entities.Tree  # Grass 或者 Tree 或者 Carrot

def work():
	nowx = get_pos_x() % 5
	nowy = get_pos_y() % 8
	basey = nowy * 4 + 3
	if nowy % 2 == 0:
		basex = nowx * 7
	else:
		basex = nowx * 7 + 3
	while True:
		move_to(basex, basey)
		while not can_harvest() and get_entity_type() != None:
			use_item(Items.Fertilizer)
		harvest()
		if pla == Entities.Grass:
			if get_ground_type() != Grounds.Grassland:
				till()
		elif pla == Entities.Carrot:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(pla)
		else:
			plant(pla)
		water()
		wanna, (x, y) = get_companion()
		move_to(x, y)
		if wanna == Entities.Grass:
			if get_ground_type() != Grounds.Grassland:
				till()
			if get_entity_type() != wanna:
				while not can_harvest():
					use_item(Items.Fertilizer)
				harvest()
		elif wanna == Entities.Carrot:
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != wanna:
				while not can_harvest() and get_entity_type() != None:
					use_item(Items.Fertilizer)
				harvest()
			plant(wanna)
		else:
			if get_entity_type() != wanna:
				while not can_harvest() and get_entity_type() != None:
					use_item(Items.Fertilizer)
				harvest()
			plant(wanna)

def main():
	move_to(0, 0)
	for i in range(8):
		for j in range(5):
			if i % 2 == 1 and j == 4:
				continue
			move_to(j, i)
			if not spawn_drone(work):
				work()

if __name__ == "__main__":
	main()