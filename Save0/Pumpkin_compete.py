def raxis(i, n=get_world_size()):
	return i // n, i % n


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





def plant_square4():
	n = 8
	dx = get_pos_x() % 8
	dy = get_pos_y() % 4
	need_check = []
	need_num = n**2 // 2
	for _ in range(n**2):
		need_check.append(True)
	while need_num > 0:
		for i in range(n**2 // 2):
			if need_check[i]:
				x, y = raxis(i, n)
				if x % 2 == 1:
					y = n - y - 1
				x += n // 2 * dx
				y += n * dy
				move_to(x, y)
				if get_ground_type() != Grounds.Soil:
					till()
				if get_entity_type() != Entities.Pumpkin:
					if can_harvest():
						harvest()
					plant(Entities.Pumpkin)
				while (not can_harvest()) and num_drones() < 6:
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
				while (not can_harvest()) and get_water() < 0.6 and need_num < 10:
					use_item(Items.Water)
				if can_harvest():
					need_check[i] = False
					need_num -= 1
	return





def main():
	while True:
		drones = []
		x, y = get_pos_x(), get_pos_y()
		x -= x % 8
		y -= y % 4
		for i in range(8):
			for j in range(4):
				move_to(7 - i + x, 3 - j + y)
				if i == 7 and j == 3:
					break
				drones.append(spawn_drone(plant_square4))
		plant_square4()
		for i in drones:
			wait_for(i)
		harvest()





if __name__ == "__main__":

	main()
	