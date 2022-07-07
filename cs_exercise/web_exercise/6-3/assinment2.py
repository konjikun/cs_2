import os
homepath =os .path.expanduser("~")
testpath = homepath + "\\Documents\\cs_exercise\\practice-6-3-1"
file = open(testpath + '\\result.txt' ,"w")
file.write("")
file.close()