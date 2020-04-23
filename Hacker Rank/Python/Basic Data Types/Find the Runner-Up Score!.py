"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given n scores.
Store them in a list and find the score of the runner-up.
"""

arr = [2, 3, 6, 6, 5]
new_list = set(arr)
new_list.remove(max(new_list))
print(max(new_list))
