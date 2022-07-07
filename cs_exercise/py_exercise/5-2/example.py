import random
results = ['大吉','中吉','小吉','凶']
for category in ['健康','仕事','恋愛','金']:
    print('今日の' + category + '運',random.choice(results))
