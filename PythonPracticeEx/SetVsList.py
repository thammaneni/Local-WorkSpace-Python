

def makeList(size):
    for i in range(size):
        list.append(input('Enter %d element for list :'%(i+1)))
    return list

def ConvertList(list):
    listSet = set()
    for i in range(len(list)):
        listSet.add(list[i])
    return listSet
    #return set(list)

list_size = int(input("Enter size of List : "))
list = []
list = makeList(list_size)

print ("List Elements : ",list)
print ("Covert to set : ",ConvertList(list))



