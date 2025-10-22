import move_utils
import multitask_utils

n = get_world_size()

def my_harvest():
	if can_harvest():
		harvest()

def my_harvestFull():
	multitask_utils.for_all(my_harvest)

def my_till():
	if get_ground_type() != Grounds.Soil:
		till()
		
def plantGrass():
	my_harvest()
	use_item(Items.Water)
	plant(Entities.Grass)

def plantGrassFull():
	multitask_utils.for_all(plantGrass)

def plantBush():
	my_harvest()
	use_item(Items.Water)
	plant(Entities.Bush)

def plantCarrot():
	if num_items(Items.Hay) < 2 ** (num_unlocked(Unlocks.Carrots)-1):
		plantGrass()
		return
	if num_items(Items.Wood) < 2 ** (num_unlocked(Unlocks.Carrots)-1):
		plantBush()
		return
	my_harvest()
	my_till()
	use_item(Items.Water)
	plant(Entities.Carrot)

def plantCarrotFull():
	multitask_utils.for_all(plantCarrot)

def plantTree():
	i = get_pos_x()
	j = get_pos_y()
	my_harvest()
	if (i+j) % 2 == 0:
		use_item(Items.Water)
		plant(Entities.Tree)
		
def plantTreeFull():
	multitask_utils.for_all(plantTree)
		
def plantPumpkin():
	my_till()
	my_harvest()
	use_item(Items.Water)
	plant(Entities.Pumpkin)

def plantPumpkinFull():
	multitask_utils.for_all(plantPumpkin)

def plantSunflower():
	my_harvest()
	my_till()
	use_item(Items.Water)
	plant(Entities.Sunflower)

def plantSunflowerFull():
	multitask_utils.for_all(plantSunflower)

def sortCactusRow():
	for row in range(n):
		# 对当前行进行冒泡排序
		for i in range(n):
			moved = False
			# 遍历整行进行相邻比较和交换
			for col in range(n):
				current_maturity = measure()
				east_maturity = measure(East)
				
				# 如果当前成熟度大于东边的，交换它们
				if current_maturity > east_maturity and col != n-1:
					swap(East)
					moved = True
				
				move(East)  # 移动到下一列
			
			# 如果这一轮没有发生交换，说明已经有序
			if not moved:
				break
		move(North)

def sortCactusCol():
	for col in range(n):
		# 对当前列进行冒泡排序
		for i in range(n):
			moved = False
			# 遍历整列进行相邻比较和交换
			for row in range(n):
				current_maturity = measure()
				north_maturity = measure(North)
				
				# 如果当前成熟度大于北边的，交换它们
				if current_maturity > north_maturity and row != n-1:
					swap(North)
					moved = True
				
				move(North)  # 移动到下一行
			
			# 如果这一轮没有发生交换，说明已经有序
			if not moved:
				break
				
		move(East)

def plantCactus():
	my_harvest()
	my_till()
	use_item(Items.Water)
	plant(Entities.Cactus)

def plantCactusCol():
	n = get_world_size()
	for _ in range(n):
		my_till()
		use_item(Items.Water)
		plant(Entities.Cactus)
		move(North)
	for _ in range(n):
		if measure(North) != None:
			if measure(North) < measure():
				swap(North)
		move(North)
	my_harvest()

def plantCactusFull():
	multitask_utils.for_all(plantCactus)
	move_utils.move_to(0, 0)

def plant_sort_CactusFull():
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