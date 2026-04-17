print("---基礎運算子整合練習 - Student Check---")

name = input("輸入名字: ")

score1 = input("輸入小考1: ")
score2 = input("輸入小考2: ")
score3 = input("輸入小考3: ")

attendance = input("輸入出席率: ")

total_score = 0.0

total_score += float(score1)
total_score += float(score2)
total_score += float(score3)  

average = total_score / 3


print("姓名: ", name)
print("總分: ", total_score)
print("平均分數: ", float(average))
print("是否通過: ", float(attendance) >= 80 and average >= 60)

# 1. 第一次修正
name = input("輸入名字: ")

score1 = float(input("輸入小考1: "))
score2 = float(input("輸入小考2: "))
score3 = float(input("輸入小考3: "))
attendance = float(input("輸入出席率: "))

total_score = 0
total_score += score1
total_score += score2
total_score += score3

# 要拿去後續計算也用「四捨五入到小數點後一位」的值
average = round(total_score / 3, 1)
  
# 先存成 passed 變數，再印出來，增加可讀性，邏輯會更清楚。
passed = average >= 60 and attendance >= 80

print("姓名:", name)
print("總分:", total_score)
print("平均分數:", average) # 不用讓型別轉換多了一層
print("是否通過:", passed)
