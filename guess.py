import random
start = input("請決定隨機數字範圍的開始值： ")
end = input("請決定隨機數字範圍的結束值： ")
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # 跟 count = count + 1
	num = input("請猜數字： ")
	num = int(num)
	if num == r:
		print("你猜對了！")
		print("你猜的次數是", count, "次")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("你猜的次數是", count, "次")
