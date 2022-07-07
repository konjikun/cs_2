def pyramid(n):
    x =1
    for i in range(1,n+1):
        print(('#'*(2*i)).center(n+n))
      
pyramid(5)