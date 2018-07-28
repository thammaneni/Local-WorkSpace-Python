def main():
    f = open("Test_File.txt","w+")
    # f = open("Test_File.txt","a")
    # for i in range(10):
    #     print("Line :",i)
    #     f.write("This is Line : "+ str(i)+"\n")
    f.write("this is content in Text file1 \n ")
    f.write("this is content in Text file2 \n")
    f = open("Test_File.txt","r")

    if f.mode == "r":
        #content =f.read()
        #fl=f.readline() # for each charector
        fl= f.readlines(); # for each line
        for x in fl:
            print("File contentLine :",x)

    f.close()

if __name__ == "__main__":
    main()
