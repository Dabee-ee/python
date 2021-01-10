# 혼자 공부하는 파이썬 30강 - 리스트 내포(List Comprehension)

# 반복문을 사용한 리스트 생성

# 1
array = []
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for i in range(0, 20, 2):
    # [0, 4, 16 ... ] 최종적으로는 제곱한 값들이 들어가게 됨.
    array.append(i * i)

print(array)

# 위와 같이 고정적인 형태가 대부분의 프로그래밍 언어에서 굉장히 많이 사용이 된다. 
# 그래서 이러한 것을 쉽게 입력할 수 있는 구문을 사람들이 만들게 되었는데,
# 그게 바로 리스트 내포이다.

# 즉, 위의 예제가 아래와 같이 표현될 수 있다.

array_2 = [ u * u for u in range(0, 20, 2)]
print(array_2)

