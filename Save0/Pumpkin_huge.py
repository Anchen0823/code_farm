import move_utils
import plant_utils
import multitask_utils

def check():
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return False
		
	return True

def main():
	clear()
	while True:
		plant_utils.plantPumpkinFull()
		for i in range(7):
			multitask_utils.for_all(check)
		harvest()
	
	
if __name__ == "__main__":
	main()