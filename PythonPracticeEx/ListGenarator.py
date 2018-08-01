def main():
    GenarateCommonList = []
    list1 = [1,2,3,4,5,6,7,8,9,12,13,4,8,15,1,3,45]
    list2 = [2,7,9,13,15,17,24,45,56,67,78,89,10]

    for i in list1:

        if i in list2:

            if i in GenarateCommonList:
                print()
            else:
                GenarateCommonList.append(i)
        else:
            print()           

    print ("Common List is : ",GenarateCommonList)

if __name__ == "__main__":
    main()
