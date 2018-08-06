
f =open("C://Users//srini//Desktop//WorkSpace//Test_File.txt","r+")
fileContent = f.read()
count=fileContent.count("Hello")
print('Count of file is %d'%count)