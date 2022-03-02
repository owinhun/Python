# 10817
# nums = list(map(int, input().split()))

# s1 = ()

# for i in range(1):
#     nums.sort(reverse = True)
#     print(nums[1])

# 2693
# import sys

# input = sys.stdin.readline

# T = int(input())

# for i in range(T):
#     nums = list(map(int, input().split()))
#     nums.sort(reverse = True)
#     print(nums[2])

# 1292
# A, B = map(int, input().split())

# a = []
# a.append(0)
# for i in range(1000):
#     for j in range(i):
#         a.append(i)

# sum = 0
# for i in range(A, B + 1):
#     sum += a[i]
# print(sum)

# 5086

# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break

#     if B % A == 0:
#         print('factor')

#     elif A % B == 0:
#         print('multiple')

#     else:
#         print('neither')

# 2442
# N = int(input())

# for i in range(1,N+1):
#     for j in range(N-i):
#         print(' ', end="")
#     for j in range(1,i*2,1):
#         print('*', end="")
#     print('')

# 10953
# T = int(input())

# for i in range(T):
#     A, B = map(int, input().split(','))

#     print(A + B)

# 2441
# N = int(input())

# for i in range(N):
#     for x in range(i):
#         print(' ', end="")
#     for y in range(N-i):
#         print('*', end="")
#     print('')

# N = int(input())

# if N % 2 == 0:
#     print('CY')
# else:
#     print('SK')