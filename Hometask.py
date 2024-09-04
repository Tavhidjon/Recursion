# 1
# def recursive_sum(n):
#     if not n:
#         return 0
#     return n[0] + recursive_sum(n[1:])
# n = [1, 2, 3, 4, 5]
# print(recursive_sum(n))



# 2
# def stringer(n, a):
#     k = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < a:
#         return k[n]
#     else:
#         return stringer(n // a, a) + k[n % a]
# c = 255
# a = 16
# print(stringer(c, a))




# 3
# def stringer(a):
#     if a == 0:
#         return ""
#     elif a < 0:
#         return "-" + stringer(-a)
#     else:
#         return stringer(a // 10) + str(a % 10)
# print(stringer(447))



# 4
# def sum(a):
#     if a == 0:
#         return 0
#     else:
#         return a % 10 + sum(a // 10)
# print(sum(300))  
# print(sum(45))   



# 5
# def sum(c):
#     if c <= 0:
#         return 0
#     else:
#         return c + sum(c - 2)
# print(sum(8))  
# print(sum(12))



#6
# def darja(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * darja(a, b - 1)
# print(darja(5,6))


#7
# def ktu(a, b):
#     if b == 0:
#         return a
#     else:
#         return ktu(b, a % b)
# print(ktu(45, 15))