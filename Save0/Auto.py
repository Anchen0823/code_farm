n = get_world_size()

def move_to(x, y):
	n = get_world_size()
	nowx = get_pos_x()
	nowy = get_pos_y()
	diffx = x - nowx
	diffy = y - nowy
	if diffx == 0 and diffy == 0:
		return
	if diffx != 0:
		abs_diffx = abs(diffx)
		if abs_diffx > n // 2:
			if diffx >= 0:
				diffx = abs_diffx - n
			else:
				diffx = n - abs_diffx
	if diffy != 0:
		abs_diffy = abs(diffy)
		if abs_diffy > n // 2:
			if diffy >= 0:
				diffy = abs_diffy - n
			else:
				diffy = n - abs_diffy
	if diffx > 0:
		for _ in range(diffx):
			move(East)
	elif diffx < 0:
		for _ in range(-diffx):
			move(West)
	if diffy > 0:
		for _ in range(diffy):
			move(North)
	elif diffy < 0:
		for _ in range(-diffy):
			move(South)
			
def my_plant(item):
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(item)
	if num_unlocked(Unlocks.Fertilizer) > 0:
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
			
def all_plant_Hay_utill(num):
	clear()
	while num_items(Items.Hay) < num:
		for i in range(n):
			for j in range(n):
				harvest()
				move(North)
			move(East)
	
def all_plant_Wood_utill(num):
	while num_items(Items.Wood) < num:
		for i in range(n):
			for j in range(n):
				my_plant(Entities.Bush)
				move(North)
			move(East)
			
def all_plant_Carrot_utill(num):
	if num > num_items(Items.Hay):
		all_plant_Hay_utill(num)
	if num > num_items(Items.Wood):
		all_plant_Wood_utill(num)
	while num_items(Items.Carrot) < num:
		for i in range(n):
			for j in range(n):
				my_plant(Entities.Carrot)
				move(North)
			move(East)

def all_plant_Pumpkin_utill(num):
	if num > num_items(Items.Carrot):
		all_plant_Carrot_utill(num)
	while num_items(Items.Pumpkin) < num:
		for i in range(n):
			for j in range(n):
				my_plant(Entities.Pumpkin)
				move(North)
			move(East)

def all_plant_Cactus_utill(num):
	if num > num_items(Items.Pumpkin):
		all_plant_Pumpkin_utill(num)
	while num_items(Items.Cactus) < num:
		for i in range(n):
			for j in range(n):
				my_plant(Entities.Pumpkin)
				move(North)
			move(East)

def moveDinosaur():
	move_to(0,0)
	change_hat(Hats.Dinosaur_Hat)
	while True:
		for i in range(n-1):
			move(East)
		move(North)
		for i in range(n):
			if i % 2 == 0:
				for _ in range(n-2):
					move(North)
			else:
				for _ in range(n-2):
					move(South)
			move(West)
		flag = move(South)
		if not flag:
			change_hat(Hats.Wizard_Hat)
			move_utils.move_to(0,0)
			change_hat(Hats.Dinosaur_Hat)

rights_of = {North:East, East:South, South:West, West:North}
lefts_of = {North:West, West:South, South:East, East:North}
opposites_of = {North:South, South:North, West:East, East:West}
def moveMaze():
	my_plant(Entities.Bush)
	use_item(Items.Weird_Substance, n * 2 ** (num_unlocked(Unlocks.Mazes) - 1))
	curr_position = (get_pos_x(), get_pos_y())
	curr_direction = North
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			clear()
			return
		
		right_direction = rights_of[curr_direction]
		if can_move(right_direction):
			move(right_direction)
			curr_direction = right_direction
			
		elif can_move(curr_direction):
			move(curr_direction)
			
		else:
			left_direction = lefts_of[curr_direction]
			if can_move(left_direction):
				move(left_direction)
				curr_direction = left_direction
			
			else:
				back_direction = opposites_of[curr_direction]
				move(back_direction)
				curr_direction = back_direction

def main():
	while num_unlocked(Unlocks.Leaderboard) == 0:

		# 解锁树丛
		while num_unlocked(Unlocks.Plant) == 0:
			unlock(Unlocks.Grass)
			unlock(Unlocks.Hats)
			unlock(Unlocks.Speed)
			unlock(Unlocks.Expand)
			unlock(Unlocks.Plant)
			all_plant_Hay_utill(10000)

		# 解锁胡萝卜
		while num_unlocked(Unlocks.Carrots) == 0:
			unlock(Unlocks.Expand)
			unlock(Unlocks.Speed)
			unlock(Unlocks.Carrots)
			all_plant_Wood_utill(10000)

		all_plant_Hay_utill(10000)
		all_plant_Wood_utill(10000)

		# 解锁肥料浇水树木
		while num_unlocked(Unlocks.Trees) == 0:
			unlock(Unlocks.Expand)
			unlock(Unlocks.Speed)
			unlock(Unlocks.Watering)
			unlock(Unlocks.Trees)
			for i in range(n):
				for j in range(n):
					my_plant(Entities.Carrot)
					move(North)
				move(East)

	all_plant_Hay_utill(50000)
	all_plant_Wood_utill(50000)
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
		all_plant_Carrot_utill(10000)

	# 解锁混合种植仙人掌
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
		all_plant_Pumpkin_utill(150000)

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
		all_plant_Cactus_utill(40000)

	while num_items(Items.Bone) < 2000000:
		if num_items(Items.Cactus) < 20000:
			all_plant_Cactus_utill(20000)
		clear()
		moveDinosaur()
	
	while num_unlocked(Unlocks.Leaderboard) == 0:
		unlock(Unlocks.Leaderboard)
		moveMaze()
