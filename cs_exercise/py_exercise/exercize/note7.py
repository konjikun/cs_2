def mpg_to_kmpl(mpg):
    return mpg / 3.785412*1.60934
def liters_needed(d,mpg):
    kmpl = mpg_to_kmpl(mpg)
    return d / kmpl
print(liters_needed(1,1))    


