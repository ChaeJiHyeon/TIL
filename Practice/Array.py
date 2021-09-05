import sys

b = []
a = list(map(int, sys.stdin.readline().split(", ")))
c = []
length = len(a)

if length <= 100:
    for i in range(1, length+1):
        b.append(i)

print(list(set(b)-set(a)))
