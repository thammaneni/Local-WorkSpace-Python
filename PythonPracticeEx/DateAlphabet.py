Number_dict = {0 :'zero', 1:'One', 2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
Length_dict ={3:'Hundred', 4:'Thousand', 5:'Thousand', 6:'lac',7:'lac'}
Tens_dict = {20:'Twenty',30:'Thirty',40:'Fourty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninghty'}

#Date conversion
def DateMonthConvert(date_val):
    if(date_val < 20):
        return Number_dict[date_val]
    else:        
        if(date_val%10 == 0):
            #print("date_val/10 ", Tens_dict[date_val/10])
            return Tens_dict[(date_val/10) * 10]
        else:
            return Tens_dict[int(date_val/10) * 10] +" "+ Number_dict[date_val % 10]

def YearConvert(year_val):
    length = len(year_val)
    if(length == 4):
        str1= Number_dict[int(int(year_val)/1000)] + " "+Length_dict[length]
        str2= Number_dict[int(int(year_val[1:])/100)] + " "+Length_dict[length-1]
        str3= DateMonthConvert(int(year_val[2:]))
        return str1+" "+str2+" "+str3
    elif(length == 3):
        str2= Number_dict[int(int(year_val)/100)] + " "+Length_dict[length-1]
        str3= DateMonthConvert(int(year_val[1:]))
        return str2+" "+str3
    else:
        return DateMonthConvert(int(year_val))
        

User_Date =input("Enter user Date :")

Date_list=User_Date.split("-")
date = int(Date_list[0])
month = int(Date_list[1])
year = Date_list[2]

print(DateMonthConvert(date)+" "+DateMonthConvert(month)+" "+YearConvert(year))




