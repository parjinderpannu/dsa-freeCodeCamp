import traceback

new_list = [1, 2, 3, 4, 5]

try:
 print(new_list[5])
except Exception as e:
 print(e)
#  traceback.print_exc()