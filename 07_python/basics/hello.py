# Python 範例：對比 C 語言的強型別
print("--- Python 基礎測試 ---")

# 1. 宣告變數（不需要指定 int, float 或 char）
name = "Chien-ting"
age = 25
gpa = 3.9
is_student = True

# 2. 格式化輸出（f-string 是最現代的寫法）
print(f"你好，我是 {name}。")
print(f"明年我就是 {age + 1} 歲了。")
print(f"目前 GPA 是 {gpa}，學生身份：{is_student}")

# 3. 動態型別示範（這在 C 語言會報錯，但在 Python 很正常）
x = 100
print(f"x 現在是數字: {x}")
x = "現在變成了字串"
print(f"x 變成: {x}")