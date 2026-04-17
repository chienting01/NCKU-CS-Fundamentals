print("--- Operators 練習 ---")

# 1) 算術運算子
a = 10
b = 3

print("[算術運算子]")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b) # 整除，取商數
print("a % b =", a % b) # 取餘數
print("a ** b =", a ** b) # 指數運算，a 的 b 次方

# 2) 比較運算子
score = 85

print("\n[比較運算子]")
print("score == 85 ->", score == 85)
print("score != 100 ->", score != 100)
print("score > 60 ->", score > 60)
print("score >= 90 ->", score >= 90)

# 3) 邏輯運算子
age = 20
is_student = True

print("\n[邏輯運算子]")
print("age >= 18 and is_student ->", age >= 18 and is_student)
print("age < 18 or is_student ->", age < 18 or is_student)
print("not is_student ->", not is_student)

# 4) 指派運算子
x = 5
print("\n[指派運算子]")
print("x 初始值 =", x)

x += 2
print("x += 2 ->", x)

x *= 3
print("x *= 3 ->", x)

x -= 4
print("x -= 4 ->", x)
