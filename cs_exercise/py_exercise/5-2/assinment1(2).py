import numpy as np
def standard_score(x):
    scores.append(x)
    mues = np.average(scores)
    a =np.std(scores)
    T = 50 + 10*(x - mues) / a
    return T

scores = [97, 83, 64, 29, 59, 28, 84, 72]    
print(standard_score(65))