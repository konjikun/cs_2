import os
homepath =os .path.expanduser("~")
print(homepath)
testpath = homepath + "\\OneDrive\\Documents\\cs_exercise\\test"
with open(testpath + '\\memo.txt' ,"r")as file:
    text = file.read()
print(text)