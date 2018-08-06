range1 = int(input("Enter Fibinocii series range : "))
list=[1,1]
list.append(a)
list.append(b)
for i in range(range1-2):
    list.append(list[i]+list[i+1])
print("Fibinocci series is : ",list)