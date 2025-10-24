import plant_utils
import move_utils

def sort_col_single():
	n = get_world_size()
	x = get_pos_x()
	for i in range(n - 1):
		swapped = False
		for j in range(n - 2, i - 1, -1):
			move_utils.move_to(x, j)
			if measure(North) < measure():
				swap(North)
				swapped = True
		if not swapped:
			return
	return

def sort_row_single():
	n = get_world_size()
	y = get_pos_y()
	for i in range(n - 1):
		swapped = False
		for j in range(n - 2, i - 1, -1):
			move_utils.move_to(j, y)
			if measure(East) < measure():
				swap(East)
				swapped = True
		if not swapped:
			return
	return

def main():
	clear()
	n = get_world_size()
	move_utils.move_to(0, 0)
	while True:
		plant_utils.plantCactusFull()


		drones = []
		for i in range(n - 1):
			move_utils.move_to(i, n - 1)
			drones.append(spawn_drone(sort_col_single))

		move_utils.move_to(n - 1, n - 1)
		sort_col_single()
		move_utils.move_to(n - 1, 0)

		for i in drones:
			wait_for(i)
		drones = []

		for i in range(n - 1):
			move_utils.move_to(n - 1, i)
			drones.append(spawn_drone(sort_row_single))

		move_utils.move_to(n - 1, n - 1)
		sort_row_single()
		move_utils.move_to(0, 0)

		for i in drones:
			wait_for(i)
		harvest()

if __name__ == "__main__":
	main()