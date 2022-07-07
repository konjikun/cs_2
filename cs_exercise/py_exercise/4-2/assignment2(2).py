def overlap(xs,ys):
    result=[]
    for i in ys:
        for n in range(len(xs)):
            if i == xs[n]:
                result.append(xs[n])
    return result
    
print(overlap([1,2,3,4,5],[2,3,5,7,11])) 