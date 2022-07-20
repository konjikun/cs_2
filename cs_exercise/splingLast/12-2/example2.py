pi =0
n=0

try:
    while True:
        pi += 4* (-1)**n/(2*n +1)
        n+=1
except KeyboardInterrupt:
    print('n=', n, ', pi=', pi)
