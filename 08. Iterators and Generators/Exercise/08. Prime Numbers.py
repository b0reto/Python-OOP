# def get_primes(*num):
#     res = []
#     flag = False
#     for current_num in range(len(num[0])):
#         if num[0][current_num] > 1:
#             for i in range(2, num[0][current_num] + 1):
#                 flag = False
#                 if num[0][current_num] % i == 0:
#                     flag = True
#                     break
#         if flag:
#             res.append(num[0][current_num])
#         else:
#             pass
#     return res



# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))





#
num = [2, 4, 3, 5, 6, 9, 1, 0]
res = []
# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
for current_num in num:
    if current_num > 1:
        # check for factors
        for i in range(2, current_num):
            flag = False
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

print(res)