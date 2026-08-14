# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 14. 14:41:47

def solution(n):
    answer = 0
    
    for i in range(n+1):
        if i % 2 == 0: 
            answer += i
    return answer