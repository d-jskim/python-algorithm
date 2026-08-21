# 수열과 구간 쿼리 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181924
# 알고리즘: 반복문
# 작성자: 학생
# 작성일: 2026. 08. 21. 17:01:50

def solution(arr, queries):
    answer = arr.copy()
    
    for idx_list in queries:
        
        i = idx_list[0]
        j = idx_list[1]

        i_val = answer[i]
        j_val = answer[j]
        
        answer[i] = j_val
        answer[j] = i_val
        
    return answer