str_in = "пара-ра-рам рам-пам-папам па-ра-па-да"
str_low = str.lower(str_in)
list = str_low.split()
func = lambda x: sum(1 for i in x if i in 'аоуиэеыёюя')
result = []
for i in list :
    result.append(func(i))
if len(set(result)) == 1 :
    print('Парам пам-пам')
else :
    print('Пам парам')