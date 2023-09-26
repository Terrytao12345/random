#產生隨機整數1~100 (不要印出來)
#讓使用者重複輸入去猜
#猜對的話 印出答對
#猜錯的話要告訴他 比答案大或小


import random

start = input('請決定起始數字')
end = input('請決定結束數字')
r = random.randint(int(start), int(end))
count = 0

while True :
	#print(r)
	count += 1 # <==> count = count + 1 
	user = input("請猜一個數字")
	if int(user) > int(r) :
		print(" user > answer　") 
	elif int(user) < int(r) :
		 print(" user < answer　") 
	else :
		if int(user) == int(r) :
			print("bingo")
			print("你猜了第", count, '次')
	#break #break放這是每猜完一次結束　並重執行　不同數字
			break #猜錯就持續猜　並到最後對時才結束
	print("你猜了第", count, '次')
