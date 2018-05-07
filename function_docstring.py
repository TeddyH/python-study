def print_max(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum' 

print_max(3, 5)
print print_max.__doc__

# 함수에 포함된 첫 논리적 명령행에 적어둔 문자열은 함수의 DocString 이라고 불리우는 것이다.
# 첫째줄의 첫문자는 대문자로, 마지막 문자는 마침표로 끝나도록 작성한다.