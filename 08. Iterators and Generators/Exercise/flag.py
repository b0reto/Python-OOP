# num = [2, 4, 3, 5, 6, 9, 1, 0]
# To take input from the user

# define a flag variable
flag = False


# prime numbers are greater than 1
# def get_primes(*args):
#     res = []
#     for current_num in range(len(args[0])):
#         flag = False
#         if args[0][current_num] <= 1:
#             continue
#         if args[0][current_num] > 1:
#             # check for factors
#             for i in range(2, args[0][current_num]):
#                 if (args[0][current_num] % i) == 0:
#                     # if factor is found, set flag to True
#                     flag = True
#                     # break out of loop
#                     break
#         # check if flag is True
#         if flag:
#             pass
#         else:
#             res.append(args[0][current_num])
#
#     return res
#
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

def get_primes(*args):
    res = []
    for current_num in args:
        flag = False
        if current_num > 1:
            # check for factors
            for i in range(2, current_num):
                if (current_num % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

        # check if flag is True
        if flag:
            pass
        else:
            res.append(current_num)

    yield res


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
