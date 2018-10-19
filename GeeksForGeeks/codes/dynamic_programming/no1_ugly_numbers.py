# https://www.geeksforgeeks.org/ugly-numbers/
# Ugly Numbers
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... shows the first 11 ugly numbers. By convention, 1 is included.
#
# Given a number n, the task is to find n'th Ugly number.
#
# Examples:
#
# Input  : n = 7
# Output : 8
#
# Input  : n = 10
# Output : 12
#
# Input  : n = 15
# Output : 24
#
# Input  : n = 150
# Output : 5832



import numpy as np

solution_set = dict()
solution_set[7] = 8
solution_set[10] = 12
solution_set[15] = 24
solution_set[150] = 5832

#o(n) solution
def genUglyNum2(n):
    if n==1:
        return 1
    else:
        arr = [1]
        n_idx = 0
        i=0
        j=0
        k=0
        while n_idx < n-1:
            ug2 = arr[i]*2
            ug3 = arr[j]*3
            ug5 = arr[k]*5

            ug = np.minimum(np.minimum(ug2, ug3), ug5)
            arr.append(ug)
            # print('%d, %d, %d'% (ug2, ug3, ug5))
            print(ug)
            if ug == ug2:
                i+=1
                # arr.append(ug2)

            if ug == ug3:
                j+=1
                # arr.append(ug3)

            if ug == ug5:
                k+=1
                # arr.append(ug5)

            n_idx+=1

        return ug


# O(nlogn) solution
def isUgly(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return isUgly(n / 2)
    elif n % 3 == 0:
        return isUgly(n / 3)
    elif n % 5 == 0:
        return isUgly(n / 5)

    return False

def genUglyNum(n):

    n_idx = 0
    num = 0
    while n_idx < n:
        num += 1
        if isUgly(num):
            # print(num)
            n_idx+=1

    return num

n = 7

print(genUglyNum2(n))
# #
# #
# exit()


is_pass = True
for k in solution_set.keys():
    # print("%d, %d" % (solution_set[k], genUglyNum2(k)))
    if genUglyNum2(k) != solution_set[k]:
        is_pass = False


if is_pass:
    print("Pass!")
else:
    print("Fail!")