d=0
distance = 0
km=10
for i in range(7):
    d+=1
    distance+=km
    km=km*1.1
print("За 7 дней спортсмен сумарно пробежит:", distance, "километров")
while distance<100:
    d+=1
    km=km*1.1
    distance += km
print('Расстояние в 100 километров будет пройдено за', d, 'дней')
while km<=20:
    d+=1
    km=km*1.1
else: print("Спортсмен будет пробегать больше 20 км начиная с", d, "дня")