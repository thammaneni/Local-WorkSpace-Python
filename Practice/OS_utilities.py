import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    print(os.name)

    print ("Item exists :"+ str(path.exists("C://Users//srini//Desktop//WorkSpace")))
    print ("Is File exists : "+str(path.isfile("C:\\Users\\srini\\Desktop\\WorkSpace\\Test_File.txt")))
    print ("Is Dir :"+str(path.isdir("C://Users//Srini//Desktop")))

    print ("Item path :" +str(path.realpath("Calendar.py")))
    print ("Item Dir and item name : "+ str(path.split(path.realpath("Calendar.py"))))

    t = time.ctime(path.getmtime("C:\\Users\\srini\\Desktop\\WorkSpace\\Test_File.txt"))
    print ("Last modification time of a File :", t)

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("C:\\Users\\srini\\Desktop\\WorkSpace\\Test_File.txt"))
    print ("The time was ", td ," since file was modified")
    print ("or Total seconds ", str(td.total_seconds()))

if __name__ == "__main__":
    main()