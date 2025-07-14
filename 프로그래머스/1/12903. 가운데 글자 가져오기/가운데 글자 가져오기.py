def solution(s):
    
    length = len(s)
    # 홀수일 때
    if length % 2 == 1:
        answer = s[length//2]
    else:
        answer = s[length//2 - 1 : length//2 + 1]
    return answer