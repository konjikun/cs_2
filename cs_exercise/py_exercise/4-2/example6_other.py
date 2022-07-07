def check_scores(pts):
    if min(pts) < 60:
            return  False
    return True
print(check_scores([90,84,35,64,98]))
