# def is_prime(num):
#     if num == 4:
#         return False
#     elif num < 6:
#         return True
#     elif num % 2 == 0 or (num % 3 == 0 or num % 5 == 0) or num % 7 == 0:
#         return False
#     else:
#         return True

# print(is_prime(13))
# no = 0
# for x in range(1,101):
#     if is_prime(x) == True:
#         no += 1
#         print(f"{no}.{x}-{is_prime(x)}")

#Final code
def prime(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True

