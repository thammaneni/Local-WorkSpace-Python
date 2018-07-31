divisor = int(input("Enter value : "))

list = range(1,100)
new_list = []
for i in list:
    if i % divisor == 0:
        new_list.append(i)

print ('The list of divisors of %d are : '%divisor, new_list)

