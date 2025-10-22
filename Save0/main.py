import plant_utils
import move_utils
import multitask_utils

n = get_world_size()

clear()
while True:
	if num_items(Items.Power) < 5000:
		while num_items(Items.Power) < 30000:
			plant_utils.plantSunflowerFull()
			plant_utils.my_harvestFull()
			clear()
	else:
		plant_utils.plantCarrotFull()