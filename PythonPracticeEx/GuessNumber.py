import random

Number = random.randint(1,9)

input = int(input("Enter User guess number :(0-9) "))

print("Game Number :",Number)
print("Player Gussing Number :",input)

if(Number == input):
    print("Exactely same..")
elif(abs(Number-input)<3):
    print("User Choice is very closer to Game Number")
else:
    print("User Choice is very too far")
