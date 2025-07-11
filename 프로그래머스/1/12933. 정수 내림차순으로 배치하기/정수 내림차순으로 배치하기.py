def solution(n):
    answer = ""
    list =  [int(num) for num in str(n)]
    for i in range(len(list)):
        max_val = max(list)
        answer += str(max_val)
        list.remove(max_val)
        
    return int(answer)