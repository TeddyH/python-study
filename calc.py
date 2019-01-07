import sys


a = 10
b = 20
c = a + b

print(c)

a = 1 + 2j
# 복소수의 실수 부분을 리턴한다.
print(a.real)

# 복소수의 허수 부분을 리턴한다.
print(a.imag)

# 복소수의 켤레복소수를 리턴한다.
print(a.conjugate())

# 복소수의 절대값을 리턴한다.
print(abs(a))