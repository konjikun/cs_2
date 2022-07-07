#オブジェクトメソッド index , append , lower,pop
nums = [1,2,3,4,]
print(nums.index(3))
nums.append(5)
print(nums.index(3),nums.index(5))
#リストにない値をindexするとerrorになる

#リストからpop(x)でx番目の要素排除
nums.pop(2)
print(nums)

#L.copy()でリストのコピー。ただしコピー元とは別のリスト