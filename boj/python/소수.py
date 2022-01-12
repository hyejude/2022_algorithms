# 수학
# https://www.acmicpc.net/problem/2581

# input() 받는 타입은 str가 default
# 모듈 sqrt() 쓰려면 math --> math.sqrt()

# ? 한 줄로 다 받는 경우는? --> a,b = input().split()
import math

m = int(input())
n = int(input())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

answer = 0
for i in range(m,n+1):
    if isPrime(i):
        if not answer:
            min_prime = i
        answer += i

if answer:
    print(answer)
    print(min_prime)
else:
    print(-1)
