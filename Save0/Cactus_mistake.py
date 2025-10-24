set_world_size(3)
n = 3
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
				if current_maturity < east_maturity and col != n-1:
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
				if current_maturity < north_maturity and row != n-1:
					swap(North)
					moved = True
				
				move(North)  # 移动到下一行
			
			# 如果这一轮没有发生交换，说明已经有序
			if not moved:
				break
				
		move(East)
		
for i in range(3):
	for j in range(3):
		till()
		plant(Entities.Cactus)
		move(North)
	move(East)

sortCactusCol()
sortCactusRow()
harvest()
