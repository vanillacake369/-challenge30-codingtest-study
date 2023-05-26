'''
출력결과 27
모듈러 연산을 진행할때 제수가 피제수보다 크면 연산결과는 피제수 그대로 나온다.
그래서 인풋값이 유일하게 제수가 더 큰 1번을 정답이라 예측하고 수행한다.

1번 f(21,34)
1번째 재귀 (34, 21) + 34
2번째 재귀 (21, 13) + 21
3번재 재귀 (13, 8)  + 13
4번째 재귀 (8, 5)   + 8
5번째 재귀 (5, 3)   + 5
6번째 재귀 (3, 2)   + 3
7번째 재귀 (2, 1)   + 2
8번째 재귀 (1, 0)   + 1
결과 34 + 21 + 13 + 8 + 5 + 3 + 2 + 1 =87
정답 87

f(123, 12)
1번째 재귀 (12, 3) + 12
2번째 재귀 (3, 0)  + 3
풀이 12 + 3
정답 15

f(2021, 4)
1번재 재귀 (4, 1) + 4
2번째 재귀 (1, 0) + 1
결과 4 + 1
정답 5

f(107, 36)
1번째 재귀 (36, 35) + 36
2번째 재귀 (35, 1)  + 35
3번째 재귀 (1, 0)   + 1
결과 36 + 35 + 1
정답 72

f(66, 60)
1번째 재귀 (60, 6) + 60
2번재 재귀 (6, 0)  + 6
결과 60 + 6
정답 66

문제 정답 : 1번
'''

def f(a, b):
    return f(b, a%b) + b if b else 0

