# 수학
# https://www.acmicpc.net/problem/24039

import math

n = int(input())
flag = False

def isPrime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def args(num):
    args_list = set()
    for i in range(2,num):
        if num % i == 0:
            if isPrime(i):
                args_list.add(i)
                args_list.add(num//i)
    args_list = list(args_list).sort()
    if args_list:
        for i in range(len(args_list)-1):
            if args_list[i]*args_list[i+1] == num:
                flag = True
                return flag



while not flag:
    n += 1
    if args(n):
        print(n)
        break
    if n == 2023:
        break 