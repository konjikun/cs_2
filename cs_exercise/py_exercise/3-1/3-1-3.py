def mpg_to_kmpl(mpg):
    return mpg *1.609 /3.785

def liters_needed(mpg,km):
    kmpl =mpg_to_kmpl(mpg)
    return km / kmpl
print(liters_needed(1,1))    
