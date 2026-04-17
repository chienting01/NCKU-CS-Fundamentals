# Exercise 02 answer
# 先閱讀 02-question.md，再在這個檔案完成實作。

original_price = int(input("商品原價: "))
check_member = bool(input("是否為會員(Y/N): "))
used_discount = bool(input("是否使用折扣(Y/N): "))

# 錯誤寫法:
# 使用 bool(input(...)) 會讓幾乎所有非空字串都變成 True，輸入 Y 或 N 都會被當成 True。

used_discount_price = original_price #C 要先宣告型別，而且通常句尾會加分號。Python 不需要宣告型別，也不用分號。
total_price = used_discount_price
fee = 60


#  if check_member == 1:
#     used_discount_price *= 0.9
#     if used_discount == 1:
#         used_discount_price -= 50
#         if used_discount_price < 0:
#             used_discount_price = 0
#         elif used_discount_price >= 1000:
#             fee = 0
# 錯誤寫法: if check_member == 1:
# 你這題輸入的是 Y/N，就應該直接判斷字串，而不是先硬轉 bool 再拿去比 1
# 免運判斷被包在使用折扣碼的分支內，導致未使用折扣碼時即使金額達標也不會免運。

total_price += fee
# total_price 先等於原價，後面只加運費，沒有確實以折扣後金額作為基礎，結果會偏高。

print ("原價: ", original_price)
print ("折扣後金額: ", used_discount_price)
print ("運費: ", fee)
print ("應付總額: ", total_price)   