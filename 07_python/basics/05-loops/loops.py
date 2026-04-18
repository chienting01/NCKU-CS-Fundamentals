print("--- Loops 練習 ---")

# 1) for 迴圈：走訪固定範圍
print("\n[for 迴圈 - 印出 1 到 5]")
for number in range(1, 6):
	print(number)
	
# number只是變數名稱，也可以改成 i、n、item
# range(start, stop) 會包含 start 但不包含 stop


# print() 預設會在結尾自動加上一個換行，所以每次 print(number) 都會跳到下一行。
# 如果不要換行，可以改成：
# for number in range(1, 6):
#     print(number, end=" ")
# 這樣會變成：1 2 3 4 5

# 2) for 迴圈：計算 1 到 100 的總和
print("\n[for 迴圈 - 1 到 100 加總]")
total = 0
for number in range(1, 101):
	total += number
print("總和:", total)

# 3) while 迴圈：倒數
print("\n[while 迴圈 - 倒數]")
countdown = 5
while countdown > 0:
	print(countdown)
	countdown -= 1
print("Go!")

# 4) break：遇到條件提早結束
print("\n[break 範例]")
for number in range(1, 11):
	if number == 6:
		print("遇到 6，停止迴圈")
		break
	print(number)

# 5) continue：跳過某些值
print("\n[continue 範例]")
for number in range(1, 6):
	if number == 3:
		continue
	print(number)
	

# 6) 練習
print("\n[小練習]")

print("\n[練習一: 印出 1 到 10]")
for i in range(1, 11):
	print (i)

print("\n練習二: 計算 1 到 100 的偶數總和")
total_even = 0
for i in range(1,101):
	if (i%2 == 0):
		total_even += i
print (total_even)

print("\n練習三: 印出九九乘法表")
for i in range(1,10):
	for j in range(1,10):
		print(f"{i}*{j}={i*j}", end="\t")
	print()
# # f-string 是 Python 用來「把變數直接放進字串」的寫法。
# 最後單獨 print() 會印一個換行。
# 通常放在內層迴圈結束後，讓下一列從新的一行開始。


print("\n練習四: 用 `while` 寫一個倒數新年快樂")
countdown = 3
while countdown >0:
	print(countdown)
	countdown -= 1
print("新年快樂")

print("\n練習五: 用 `continue` 跳過偶數，只印奇數")
for i in range(1,11):
	if(i%2==0):
		continue
	print(i)