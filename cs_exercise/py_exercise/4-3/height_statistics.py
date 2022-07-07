data = [172.8, 156.9, 175.9, 156.1, 166.8, 161.9, 166.9, 176, 159.8, 164, 160.3, 153.5, 174.1, 172.2, 172.7, 166.7, 173.7, 158, 172.7, 155.9]

print(data)

#標本平均
def mean(data):
     return sum(data) / len(data)

#標本分散

def variance(data):
    x = 0
    result = 0
    for i in range (len(data)):
        result += (data[i] - mean(data)) **2   
    result =result / mean(data)
    return result






