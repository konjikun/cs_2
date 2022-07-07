import os
homepath =os .path.expanduser("~")
testpath = homepath + "\\Documents\\cs_exercise"
file = open(testpath + '\\memo.txt' ,"r")
file.write("INIAD Taro")
file.close()