def solution(nums):
    # 최대로 가져갈 수 있는 수
    possive_values = len(nums) // 2
    
    # 중복 제거한 폰켓몬 집합의 길이
    nums_set_len = len(set(nums))
    
    if nums_set_len >= possive_values:
        return possive_values
    else:
        return nums_set_len