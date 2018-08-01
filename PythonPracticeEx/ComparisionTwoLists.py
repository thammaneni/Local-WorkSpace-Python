# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# #other way
# #c = [i for i in a for j in b if i == j]  

# #printing common values from two lists
# c = [i for i in a if i in b]

# print (c)
# ===========================

import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16) #pics only unique value list
#random.choices() picks duplicate values
print (a)
print (b)
result = [i for i in set(a) if i in b]
print (result)