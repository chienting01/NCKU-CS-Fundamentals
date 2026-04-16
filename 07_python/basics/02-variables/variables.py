# 02-variables: 變數與基本資料型態
print("--- Variables 練習 ---")

# 1) 宣告不同型態的變數
name = "Andy"            # str
age = 28                  # int
height = 172.5            # float
is_student = True         # bool
# 變數名稱規則：只能包含字母、數字和底線，且不能以數字開頭
# 練習
major = "Computer Science" # str
age_str = "28"

# 2) 印出變數內容
print("姓名:", name)
print("年齡:", age)
print("身高:", height)
print("是否為學生:", is_student)

print("主修:", major)
print("年齡(字串)", age_str)

# 3) 簡單運算與更新
next_year_age = age + 1
print("明年年齡:", next_year_age)

next_year_age_str = str(int(age_str) + 1) # 先將 age_str 轉為 int，運算後再轉回 str
print("明年年齡(字串):", next_year_age_str)


# 4) 用 type() 觀察型態
print("name 的型態:", type(name))
print("age 的型態:", type(age))
print("height 的型態:", type(height))
print("is_student 的型態:", type(is_student))

print("major 的型態:", type(major))
print("age_str 的型態:", type(age_str))