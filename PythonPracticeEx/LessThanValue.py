inp = int(input("Enter user values : "))

list = [4,6,9,12,45,32,123,2,6,0,23,54,81,40,15,67,73,56]
new_list = []
list_len = len(list)
print ('The length of list is : %d ' %list_len)
k=0
for i in list:
    if i < inp:
        new_list.append(i)
    else:
        print()

print ('List of values which are less than %d is' %inp , new_list)