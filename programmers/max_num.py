from itertools import combinations

def solution(number, k):
    num_list = []
    for unit in set(combinations(number,len(number)-k)):
        num_list.append(int(''.join(unit)))
    return max(num_list)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))