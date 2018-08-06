inputString = input("Enter some sentence.. : ")
list = inputString.split(" ")

print("Your Sentence is : ", " ".join(list[::-1])) # reverse String with join function to add spacess between list words.

