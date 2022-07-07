def check_scores(pts):
    for i in pts:
        if i < 60:
            return  False
    return True
print(check_scores({90,84,35,64,98}))
