# 배열의 길이에 따라 다른 연산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 알고리즘: 함수(메서드)
# 작성자: 학생
# 작성일: 2026. 08. 21. 17:28:42

def solution(arr, n):
    
    # arr 길이
    arr_len = len(arr)
    
    if arr_len % 2 == 1: # 홀수
        for i in range(0, len(arr), 2):
            arr[i] += n
    else: # 짝수
        for i in range(1, len(arr)+1, 2):
            arr[i] += n
    
    return arr