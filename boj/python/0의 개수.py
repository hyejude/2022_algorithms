# 수학
# https://www.acmicpc.net/problem/11170 맞았습니다!!
# 한 줄로 여러 개 입력 받기 
# 더 좋은 로직이 있을지...

count = int(input())
answer_list = []

for i in range(count):
    answer = 0
    n,m = map(int,input().split())
    for j in range(n,m+1):
        if '0' in str(j):
            answer += str(j).count('0')
    answer_list.append(answer)

for a in answer_list:
    print(a)