def quad_eq(a,b,c):
    D = ((b ** 2) -(4 * a * c)) ** 0.5
    ans1 = (-b + D) / (2 *a)
    ans2 = (-b - D) / (2 * a)
    return max(ans1,ans2)
print(quad_eq(-2,1,1))    

