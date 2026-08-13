# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 13. 13:56:24

def solution(n, k):
    answer = 0
    price = 12000 * n + 2000 * k
    discount = (n//10) * 2000
    answer = price - discount
    return answer