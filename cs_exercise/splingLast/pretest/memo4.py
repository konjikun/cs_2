class Sprint:
    def __init__(self, tm, cn):
        self.time = tm
        self.country = cn

    def is_passed(self, cut):
        if self.time <= cut:
            return 'P'
        else:
            return 'NP'

bolt = Sprint(9.86, 'JAM')
asuka = Sprint(10.17, 'JPN')
print(bolt.country)
print(asuka.time)
print(bolt.is_passed(10.01))
print(bolt.is_passed(9.86))
ret = asuka.is_passed(10.01)
print(ret)