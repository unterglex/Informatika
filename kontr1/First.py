'''3(5) Упорядочить по возрастанию элементы массива с четныи индексами (остальные элементы оставить на своих местах) '''
m = [1, 10, 3, 6, 5, 8, 7, 4, 9, 2]
n=[]
k=[]
for i in range(len(m)):
    if i%2==1:
        n.append(m[i])
    else: k.append(m[i])
for i in range(len(n)):
    for l in range(i+1, len(n)):
        if n[i]>=n[l]:
            chc=n[i]
            n[i]=n[l]
            n[l]=chc
print(n+k)