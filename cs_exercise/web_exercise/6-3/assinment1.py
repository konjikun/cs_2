import os
homepath =os .path.expanduser("~")
print(homepath)
testpath = homepath + "\\Documents\\cs_exercise\\practice-6-3-1"
print(testpath)
os.makedirs(testpath,exist_ok=True)

homepath =os .path.expanduser("~")
testpath = homepath + "\\Documents\\cs_exercise\\practice-6-3-1"
file = open(testpath + '\\result.txt' ,"w")
file.write("")
file.close()

homepath =os .path.expanduser("~")
testpath = homepath + "\\Documents\\cs_exercise\\practice-6-3-1"
file = open(testpath + '\\result.txt' ,"w")
file.write("Aren Sintani")
file.close()