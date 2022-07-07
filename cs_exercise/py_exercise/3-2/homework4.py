def double(xs):
    i = 0
    replica = xs.copy()
    while i < len(xs):
        replica[i] *= 2
        i += 1
    return replica

# 動作確認
numbers = [1,2,3]
print(double(numbers))
print(double(numbers))