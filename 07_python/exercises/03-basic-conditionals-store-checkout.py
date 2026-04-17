# Exercise 03
# Title: Basic Exercise - Conditionals - Store Checkout
#
# Goal:
# Practice condition branches with arithmetic and logical rules.
#
# Scenario:
# Build a store checkout calculator.
# User inputs:
# 1) original amount
# 2) member status (yes/no)
# 3) discount code usage (yes/no)
#
# Rules:
# 1) If member is yes, apply 10% off (90% of original amount).
# 2) If discount code is yes, subtract 50 from current amount.
# 3) Final discount amount cannot be below 0.
# 4) Shipping fee:
#    - free shipping if discounted amount >= 1000
#    - otherwise shipping fee is 60
# 5) Print:
#    - original amount
#    - discounted amount
#    - shipping fee
#    - final payable amount
#
# Required operators:
# - Arithmetic: +, -, *
# - Comparison: >=
# - Logical: and/or (at least one should appear)
# - Assignment: -= (or +=)
#
# Hint:
# - You can use current_total as your running amount variable.
# - Consider using max(current_total, 0) logic with if to avoid negative value.
#
# Bonus:
# - Print one extra message by level:
#   - final payable >= 2000: "VIP Order"
#   - final payable >= 1000: "Standard Order"
#   - else: "Small Order"
