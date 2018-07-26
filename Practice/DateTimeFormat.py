from datetime import datetime

t = datetime.now()
print (t.strftime("The current year is : %Y"))
print (t.strftime("The current date is : %d"))
print (t.strftime("The current month is : %B"))
print (t.strftime("The current weekday is : %A"))

print (t.strftime("The Local Date and Time is : %c"))
print (t.strftime("The Local date is : %x"))
print (t.strftime("The Local time is : %X"))

print (t.strftime("The current time is : %I:%M:%S %p"))