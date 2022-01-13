import sys

# print(sys.argv)
# cmd 실행: python myargv.py 1 2 3 4 5
# ['myargv.py', '1', '2', '3', '4', '5']

li = sys.argv[1:]
print("li=", li)

li = list(map(int, li))
print("li=", li)

print("입력값의 총합 =", sum(li))

