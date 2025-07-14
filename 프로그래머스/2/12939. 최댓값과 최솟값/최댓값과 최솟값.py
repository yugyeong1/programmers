def solution(s):
    list = [int(num) for num in s.split(' ')]
    return f'{min(list)} {max(list)}'