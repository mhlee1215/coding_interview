#https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


#dp
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        arr = [0, 1]
        n_idx = 2
        while n_idx < n:
            arr.append(arr[n_idx-2]+arr[n_idx-1])
            n_idx+=1

    return arr[-1]

#dp space opt
def fibonacci2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        n_idx = 2
        while n_idx < n:
            c = a+b
            a = b
            b = c
            n_idx+=1

    return c




n = 10
print(fibonacci2(n))