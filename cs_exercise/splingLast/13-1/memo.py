def get_recip(xs):
    try:
       return  [1/i for i in xs]
    except:
        return None

ret = get_recip( [ 2.0, 0.8, 'abc' ] )
print(ret)