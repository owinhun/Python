# import sys

# n = sys.stdin.readline()

# print(n + '??!')

# n = int(input())

# for i in range(1,10):
#     print(n, '*' ,i '=' , n*i )

# n = int(input())

# for i in range(1,10):
#     print(n, '*', i, '=', n*i)

# import sys

# for i in range(5):
#     a,b = map(int,sys.stdin.readline().split())

#     print(a+b)

# import sys

# l1 = []
# for i in range(9):
#         n = sys.stdin.readline()
#         l1.append(n)

# max(l1)
# min(l1)

# n = int(input())

# for i in range(n):
#     print('{:>n}'.format('*' * (i+1)))

# n = int(input())
# for i in range(1, n+1):
# 	print(' '*(n-i) + '*'*i)

# import sys
# n = int(sys.stdin.readline())
# l1 = []
# a = 0
# for i in range(n):
#     a = int(sys.stdin.readline())
#     l1.append(a)
# l1.sort()
# for i in l1:
#     print(i)

# a = int(input())
# b = int(input())

# print(a+b)

# import sys

# n = int(sys.stdin.readline())
# l1 = []

# for i in range(n):
#     l1.append(list(map(int, sys.stdin.readline().split())))
# l1.sort(key=lambda x : (x[0], x[1]))

# for i in l1:
#     print(i[0],i[1])

# n = int(input())

# l1 = []
# for i in range(n):
#     string = input()
#     l1.append(string)

# s1 = set(l1)
# l2 = list(s1)
# l2.sort()
# l2.sort(key=len)  

# for i in l2:
#     print(i)

# while True:
#     a,b,c = map(int, input().split())

#     result = c**2 == a**2 + b**2

#     if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == c**2 + a**2:
#         if a == b == c == 0:
#             break
#         else:
#             print('right')
#             pass
#     else:
#         print('wrong')

# n = int(input())

# l1 = []
# for i in range(n):
#     age, name = input().split()
#     l1.append([int(age), name])

# l1.sort(key = lambda x : int(x[0]))

# for i in l1:
#     print(i[0],i[1])

# x, y, w, h = map(int, input().split())

# print(min(x, y, w - x, h - y))

# n = int(input())
# l1 = []

# for i in str(n):
#     l1.append(int(i))

# l1.sort(reverse=True)
        
# for i in l1:
#     print(i, end = "")
