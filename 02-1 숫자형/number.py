# 정수형
a = -178
print(a)

# 실수형
a = 3.14E-2
print(a)

# n진수
a = 0b1001
print(a)
a = 0o11
print(a)
a = 0xabc
print(a)
print(10*16**2 + 11*16**1 + 12)

# 연산
a = 3; b = 4
print(a + b)
print(a * b)
print(a**b)
print(3*3*3*3)
print(a / b)
print(a//b)
print(a % b)
print(7 % 3)

# 파이썬에서의 정수(ingeger)
i = 9999999999999999999999999999999999999999999999999999999999
print(i)
print(i + 1)
print(type(i)) # 객체의 자료형 알아내기 type(값/객체)
print(i.bit_length()) # arbitrary-precision <-> fixed-precision

# 파이썬에서의 실수(float)
print(3.5 + 2.1)
print(0.1 + 0.2) # 부동소수점은 실수를 정확히 표현할 수 없는 문제
print(4.3 - 2.7) # = 1.6 ?
                 # 컴퓨터에서는 숫자를 비트로 표현하는데
                 # 실수는 유한개의 비트로 정확하게 표현할 수가 없다
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 15) == 0.3)

# 파이썬에서의 형변환 및 연산
print(int(3.14))
print(5.5 + 5)
print(float(5))
print(float("3.14"))
print("111" * 3)
print("111\n" * 3)
print("111" + 1) # TypeError: can only concatenate str (not "int") to str

