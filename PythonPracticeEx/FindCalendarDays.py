Flag= True
def findCalenderDays(inpDays):
    years = int(inpDays/365)
    weeks = int(inpDays%365)/7
    days = int(inpDays%365)%7
    print('%d years '%years, '%d weeks' %weeks, '%d days '%days)
        
while Flag:
    try:
        inputDays=int(input("Enter no.of Days : "))
        Flag = False
        findCalenderDays(inputDays)
        continue
    except ValueError:
        print("Not an integer!")
        continue
