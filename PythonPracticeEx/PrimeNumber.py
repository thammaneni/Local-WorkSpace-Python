
def get_Number():
    return int(input("Enter user number to check prime or not : "))

def divisors_range(inp):
    return int(inp/2)

def check_Division(i,j):
    #print(i,j)
    if(i%j == 0):
        return True
    else:
        return False
flag = True
inp = get_Number()

if( inp < 2):
    print("Not prime")
    flag = False
    
elif(inp == 2):
    print("Number is Prime")
    flag = False
    
else:
    for i in range(divisors_range(inp)):
        if check_Division(inp,i+2):
            print("Not Prime")
            flag = False
            break
        
#print(flag)
if (flag):
    print ("Number is Prime")


