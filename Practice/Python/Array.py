import sys

b = []
a = list(map(int, sys.stdin.readline().split(", ")))
length = len(a)

# 길이가 100을 넘으면 다시 적는다.
while length > 100:
    # 초기화를 하는 clear메소드보다 []가 실행 속도가 빠르다.
    a = []
    a = list(map(int, sys.stdin.readline().split(", ")))
    length = len(a)

# 갯수가 조건을 만족한다면 a의 갯수만큼 b는 순서대로 들어간 리스트가 만들어 질 것이다.
for i in range(1, length+1):
    b.append(i)

# 여기서 set의 순서를 바꿔서 생각해버려서 계속 다른 값이 나왔다.
# 좀 더 잘 생각해 볼 것!
print(list(set(b)-set(a)))
