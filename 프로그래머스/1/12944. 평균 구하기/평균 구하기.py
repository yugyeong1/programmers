def solution(arr):
    result = 0
    for num in arr:
        result += num
    
    return result / len(arr)