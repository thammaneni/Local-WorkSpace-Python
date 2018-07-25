var1 = 10
print (var1)

var2 = 20

print(var2)

def display():
    global var1
    var1 = 15
    print("This is function defination :", var1)

display()
print(var1)


