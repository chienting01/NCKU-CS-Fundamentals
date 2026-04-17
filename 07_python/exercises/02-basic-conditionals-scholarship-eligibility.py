# Exercise 02
# Title: Basic Exercise - Conditionals - Scholarship Eligibility
#
# Goal:
# Practice arithmetic operators, comparison operators, logical operators,
# assignment operators, and if/elif/else flow control in one program.
#
# Scenario:
# Build a scholarship eligibility checker.
# User inputs:
# 1) name
# 2) three quiz scores (can be decimals)
# 3) attendance rate (0-100)
# 4) violation record (yes/no)
#
# Requirements:
# 1) Create total_score with initial value 0.
# 2) Use += to accumulate three quiz scores into total_score.
# 3) Compute average_score = total_score / 3.
# 4) Determine eligibility with ALL conditions:
#    - average_score >= 85
#    - attendance >= 90
#    - no violation record
# 5) Print:
#    - name
#    - total_score
#    - average_score (rounded to 1 decimal)
#    - eligibility result (Eligible / Not eligible)
#
# Required operators:
# - Arithmetic: +, /
# - Comparison: >=
# - Logical: and
# - Assignment: +=
#
# Hint:
# - Use a boolean variable, e.g. is_eligible, to make logic readable.
# - If violation input is "yes", it should fail eligibility.
#
# Bonus:
# - Add one more branch:
#   If average_score >= 95 and attendance == 100, print "Top Candidate".
