import re
def solution(phone_number):
    return re.sub('.', '*', phone_number[:-4]) + phone_number[-4:]