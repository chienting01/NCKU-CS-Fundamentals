# 題目名稱：
# 基礎運算子整合練習 - Student Check

# 題目目標：
# 請練習同時使用四類運算子：
# 1) 算術運算子
# 2) 比較運算子
# 3) 邏輯運算子
# 4) 指派運算子

# 題目情境：
# 你要做一個「學生是否通過」的小程式。
# 使用者會輸入：
# - 姓名
# - 三次小考分數（整數）
# - 出席率（整數，0 到 100）

# 實作要求：
# 1. 建立 total_score，初始值為 0
# 2. 用 += 依序把三次分數加到 total_score
# 3. 算出 average = total_score / 3
# 4. 判斷 average 是否 >= 60
# 5. 判斷 attendance 是否 >= 80
# 6. 用 and 判斷是否同時滿足兩個條件
# 7. 印出：
#    - 姓名
#    - 總分
#    - 平均分數
#    - 是否通過（True 或 False）

# 必須出現的運算子：
# - 算術：+, /
# - 比較：>=
# - 邏輯：and
# - 指派：+=

# 輸出範例（僅示意）：
# 姓名: Andy
# 總分: 240
# 平均: 80.0
# 通過: True


name = input("輸入名字: ")

score1 = input("輸入小考1: ")
score2 = input("輸入小考2: ")
score3 = input("輸入小考3: ")

attendance = input("輸入出席率")

total_score = 0.0

total_score += float(score1)
total_score += float(score2)
total_score += float(score3)  

average = total_score / 3


print("姓名: ", name)
print("總分: ", total_score)
print("平均分數: ", float(average))
print("是否通過: ", float(attendance) >= 80 and average >= 60)

