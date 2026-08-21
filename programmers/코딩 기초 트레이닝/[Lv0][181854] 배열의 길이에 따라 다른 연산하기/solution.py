def solution(arr, n):
    
    # arr 길이
    arr_len = len(arr)
    
    if arr_len % 2 == 1: # 홀수
        for i in range(0, len(arr), 2):
            arr[i] += n
    else: # 짝수
        for i in range(1, len(arr), 2):
            arr[i] += n
    
    return arr