'''
[[60, 50], [30, 70], [60, 30], [80, 40]]	4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133

60 50
70 30
60 30
80 40 >> 80 50

10 7 
12 3
15 8
14 7
15 5 >> 15 8 >> 120

1. sort
2. list_left, list_right
3. return max(list_left) * max(list_right)
'''
def solution(sizes):
    list_left, list_right = [],[]

    for s in sizes:
        s.sort()
        list_right.append(s.pop())
        list_left.append(s.pop())

    return max(list_left) * max(list_right)
    
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))



