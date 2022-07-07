def overlap(xs,ys):
    result =[]
    return [x for x in xs if x in ys ]

print(overlap([1,2,3,4,5],[2,3,5,7,11]))
