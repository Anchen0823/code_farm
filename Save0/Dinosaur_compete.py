import move_utils

n = get_world_size()

def main():
	move_utils.move_to(0,0)
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

if __name__ == "__main__":
	main()