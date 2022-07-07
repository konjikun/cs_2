import os
homepath =os .path.expanduser("~")
print(homepath)
testpath = homepath + "\\Documents\\cs_exercise\\test"
print(testpath)
os.makedirs(testpath,exist_ok=True)