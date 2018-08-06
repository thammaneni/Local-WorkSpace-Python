import os
def directory(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension):
      count += 1
  return count

print("No.of files in Dir : ",directory("C:\\Users\\srini\\Desktop\\WorkSpace\\Practice",".py"))

print("No.of files in Dir : ",directory("C:\\Users\\srini\\Desktop\\WorkSpace\\PythonPracticeEx",".py"))