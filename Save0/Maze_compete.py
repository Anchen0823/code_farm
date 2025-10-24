n = 5
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

def init_maze():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance)


def add_ws():
	while num_items(Items.Gold) < 9863168:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance, substance)
			for i in range(6):
				if get_entity_type() == Entities.Treasure:
					use_item(Items.Weird_Substance, substance)
					if i == 5:
						harvest()
				else:
					break
				

def init_drones():
	for i in range(n):
		for j in range(n):
			spawn_drone(add_ws)
			move(East)
		move(North)
		

	
def main():
	set_world_size(n)
	init_drones()
	
	while num_items(Items.Gold) < 9863168:
		if measure() == None:
			init_maze()

	
if __name__ == "__main__":
	main()