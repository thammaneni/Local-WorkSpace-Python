import random

# def functionget(ind):
#     return list2[ind]
# list2 = random.sample(range(11,50),10)
# print(list2)

# new_list = []
# new_list.append(functionget(0))
# new_list.append(functionget(-1))
# #new list with first and last index of List2
# print (new_list)
#=========================================
list2 = random.sample(range(11,50),10)
print (list2)
def fun(list2):
    return [list2[0],list2[-1]] #returns list
    # return (list2[0],list2[-1]) # returns touple

print (fun(list2))