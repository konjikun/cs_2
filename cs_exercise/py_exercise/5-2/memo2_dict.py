translator ={'apple':'リンゴ','banana':'バナナ'}
#存在しないキーを打つとエラーになる。エラーにしたくない場合は
print(translator.get('orange'))#みたいにgetいれる

#追加は
translator['orange'] ='みかん'

#削除は
del translator['banana']

'apple' in translator 
#True

'apple' not in translator
#False

# in はリストやタプルでも使える！

#キーを列挙
#for key in dict:

#値を列挙
#for 値 in dict.values()

#キーと値の両方を列挙
#for key , 値 in dict.idems():