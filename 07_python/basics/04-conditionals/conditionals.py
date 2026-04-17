print("--- Conditionals 練習 ---")

# 1) 成績等第判斷
score = float(input("請輸入分數: "))

if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
elif score >= 60:
	grade = "D"
else:
	grade = "F"

print("成績等第:", grade)

# 2) 年齡是否成年
age = int(input("請輸入年齡: "))

if age >= 18:
	print("成年")
else:
	print("未成年")

# 3) 溫度冷熱判斷
temperature = float(input("請輸入目前溫度: "))

if temperature >= 30:
	print("天氣偏熱")
elif temperature >= 20:
	print("天氣舒適")
else:
	print("天氣偏冷")
