# 基础功能函数 基础种植 干草 灌木
def move_to(x, y):
	dx = x - get_pos_x()
	dy = y - get_pos_y()
	while(dx):
		dx = x - get_pos_x()
		if(dx > 0):
			move(East)
		elif(dx < 0):
			move(West)
	while(dy):
		dy = y - get_pos_y()
		if(dy > 0):
			move(North)
		elif(dy < 0):
			move(South)
			
def my_plant(item):
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
		plant(item)
	else:
		plant(item)
	if num_unlocked(Unlocks.Fertilizer) > 0:
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer) 

def all_plant_Hay_until(num):
	clear()
	while num_items(Items.Hay) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				harvest()
				move(North)
			move(East)
			
def all_plant_Sunflower_until(num):
	clear()
	while num_items(Items.Power) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Sunflower)
				move(North)
			move(East)
			
def all_plant_Bush_until(num):
	while num_items(Items.Wood) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Bush)
				move(North)
			move(East)

# 基础种植 胡萝卜 南瓜 仙人掌
def all_plant_Carrot_until(num):
	if num > num_items(Items.Hay):
		all_plant_Hay_until(num)
	if num > num_items(Items.Wood):
		all_plant_Bush_until(num)
	while num_items(Items.Carrot) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Carrot)
				move(North)
			move(East)
			

def all_plant_Pumpkin_until(num):
	if num > num_items(Items.Carrot):
		all_plant_Carrot_until(num)
	while num_items(Items.Pumpkin) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Pumpkin)
				move(North)
			move(East)
			
def all_plant_Cactus_until(num):
	if num > num_items(Items.Pumpkin):
		all_plant_Pumpkin_until(num)
	while num_items(Items.Cactus) < num:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Cactus)
				move(North)
			move(East)

# 恐龙贪吃蛇
def plant_Dinosaur():
	if not can_move(East) and not can_move(West) and not can_move(South) and not can_move(North) :
		change_hat(Hats.Gray_Hat)

def def_Dinosaur():
	oldbone = num_items(Items.Bone)
	newbone = oldbone
	change_hat(Hats.Gray_Hat)
	while get_pos_y()>0:
		move(North)
	while get_pos_x()>0:
		move(East)
	change_hat(Hats.Dinosaur_Hat)
	while newbone == oldbone:
		while newbone == oldbone:
			while get_pos_y()  <get_world_size()-1:
				move(North)
				plant_Dinosaur()
				newbone = num_items(Items.Bone)
			move(East)
			plant_Dinosaur()
			while get_pos_y()>1:
				move(South)
				plant_Dinosaur()
			move(East)
			plant_Dinosaur()
			if get_pos_x()== get_world_size()-1 and get_pos_y()==1:
				move(South)
				plant_Dinosaur()
				while get_pos_x()>0:
					move(West)
					plant_Dinosaur()

# 迷宫
dirs = [East, South, West, North]
dirs_index = {East: 0, South: 1, West: 2, North: 3}
def get_right_dir(dir):
	return dirs[(dirs_index[dir] + 1) % 4]
def get_left_dir(dir):
	return dirs[(dirs_index[dir] - 1) % 4]
def def_mazes():
	# 生成迷宫
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	# 沿着墙走
	dir = North
	while True:
		# 能往右走就往右
		if can_move(get_right_dir(dir)):
			dir = get_right_dir(dir)
			move(dir)
		else:
			dir = get_left_dir(dir)
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		
# 主程序 逐步解锁
while num_unlocked(Unlocks.Leaderboard) == 0:
	
	# 解锁树丛
	while num_unlocked(Unlocks.Plant) == 0:
		unlock(Unlocks.Grass)
		unlock(Unlocks.Hats)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Expand)
		unlock(Unlocks.Plant)
		all_plant_Hay_until(10000)
		
	# 解锁胡萝卜
	while num_unlocked(Unlocks.Carrots) == 0:
		unlock(Unlocks.Expand)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Carrots)
		all_plant_Bush_until(10000)
			
	all_plant_Hay_until(10000)
	all_plant_Bush_until(10000)
	# 解锁 肥料 浇水 树木
	while num_unlocked(Unlocks.Trees) == 0:
		unlock(Unlocks.Expand)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Watering)
		unlock(Unlocks.Trees)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				my_plant(Entities.Carrot)
				move(North)
			move(East)
			
	all_plant_Hay_until(50000)
	all_plant_Bush_until(50000)
	# 解锁南瓜
	while num_unlocked(Unlocks.Pumpkins) == 0:
		unlock(Unlocks.Expand)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Carrots)
		unlock(Unlocks.Fertilizer)
		unlock(Unlocks.Watering)
		unlock(Unlocks.Trees)
		unlock(Unlocks.Sunflowers)
		unlock(Unlocks.Pumpkins)
		all_plant_Carrot_until(10000)
		

	# 解锁 混合种植 仙人掌
	while num_unlocked(Unlocks.Polyculture) == 0:
		unlock(Unlocks.Grass)
		unlock(Unlocks.Expand)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Carrots)
		unlock(Unlocks.Fertilizer)
		unlock(Unlocks.Watering)
		unlock(Unlocks.Trees)
		unlock(Unlocks.Pumpkins)
		unlock(Unlocks.Cactus)
		unlock(Unlocks.Polyculture)
		all_plant_Pumpkin_until(150000)
		
	# 解锁恐龙
	while num_unlocked(Unlocks.Dinosaurs) == 0:
		unlock(Unlocks.Grass)
		unlock(Unlocks.Expand)
		unlock(Unlocks.Speed)
		unlock(Unlocks.Carrots)
		unlock(Unlocks.Fertilizer)
		unlock(Unlocks.Watering)
		unlock(Unlocks.Trees)
		unlock(Unlocks.Pumpkins)
		unlock(Unlocks.Mazes)
		unlock(Unlocks.Cactus)
		unlock(Unlocks.Polyculture)
		unlock(Unlocks.Dinosaurs)
		unlock(Unlocks.Mazes)
		all_plant_Cactus_until(40000)
	
	# 走恐龙路径
	while num_items(Items.Bone) < 2000000:
		if num_items(Items.Cactus) < 20000:
			all_plant_Cactus_until(20000)
		clear()
		def_Dinosaur()
		
	# 解锁排行榜
	while num_unlocked(Unlocks.Leaderboard) == 0:
		unlock(Unlocks.Leaderboard)
		if num_items(Items.Power) < 1000:
			all_plant_Sunflower_until(20000)
		clear()
		def_mazes()