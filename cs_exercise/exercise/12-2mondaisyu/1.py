def count_caps(words):
  lists=[]
  result =0
  for s in range(65,92):
    for i in words:
        if chr(s) == i[0]:
            result+=1
  
  
  return result

in_list = ['Joel', 'drums','Pentatonix','1D','guitar']
print(count_caps(in_list))