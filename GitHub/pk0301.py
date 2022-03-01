# print('Hello world')

M = int(input())
N = int(input())

l1 = []

for i in range(M,N+1):
    er = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                er += 1
                break
        if er == 0:
            l1.append(i)

if len(l1) > 0:
    print(sum(l1))           
    print(min(l1))

else:
    print(-1)