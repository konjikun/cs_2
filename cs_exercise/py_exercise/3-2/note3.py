for s in ['tomato','orange','apple']:
    print(s)
ametal = ['Li','Na','K']
halogen = ['F','Cl','br']

#ネスト可能、ただしインデント注意
for a in ametal:
    for h in halogen:
        print(a+h)