import plant_utils

rights_of = {North:East, East:South, South:West, West:North}
lefts_of = {North:West, West:South, South:East, East:North}
opposites_of = {North:South, South:North, West:East, East:West}

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

def moveMaze():
	plant_utils.plantBush()
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
			move_to(0,0)
			change_hat(Hats.Dinosaur_Hat)