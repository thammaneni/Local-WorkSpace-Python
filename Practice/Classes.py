class myClass():
    def method1(self):
        print("myClass Method1")
    def method2(self,message):
        print("Myclass Method2 ", message)

class AnotherClass(myClass):
    
    def method3(self):
        myClass.method1(self)
        print("This is Another class method3")
    
    def method4(self,message):
        print("This is method4 ", message)


def main():
    c = myClass()
    c.method1()
    c.method2("This Class method2")

    d = AnotherClass()
    d.method3()
    d.method4("Another class")


if __name__ == "__main__":
    main()
    