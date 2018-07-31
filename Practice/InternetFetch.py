import urllib.request

def main():
    webUrlData= urllib.request.urlopen("https://www.google.com")
    print("Result code :" +str(webUrlData.getcode())
    data = webUrlData.read()
    print(data)


if __name__ == "__main__":
  main()

