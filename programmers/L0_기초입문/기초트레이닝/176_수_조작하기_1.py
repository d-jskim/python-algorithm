# 수 조작하기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 알고리즘: 조건문
# 작성자: 학생
# 작성일: 2026. 08. 13. 17:57:21

def solution(n, control):
    answer = n
    
    for i in range(len(control)):
        if control[i] == "w": answer += 1
        elif control[i] == "s": answer-= 1
        elif control[i] == "d": answer += 10
        elif control[i] == "a": answer -= 10
    
    return answer