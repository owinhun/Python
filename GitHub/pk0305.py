# 1929
# M, N = map(int, input().split())

# for i in range(M,N+1):
#     if i == 1:
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j == 0:
#             break
#     else:
#         print(i)

# 1912

# n = int(input())
# a = list(map(int, input().split()))

# for i in range(1,n):
#     a[i] = max(a[i], a[i-1] + a[i])

# print(max(a))