N = 20  # 마이쮸의 개수

queue = [(1,0)]  # 초기화

# (0,0) [0]: 사람 번호, [1]: 직전까지 받았던 마이쮸의 개수

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0)  # 받으러 온 사람, 저번까지 받은 개수

    last_people = num  # 마지막으로 받으러 온 사람
    cnt += 1  # 저번 보다 하나 더 챙긴다

    N -= cnt
    new_people += 1

    queue.append((num, cnt)) # 맨 뒤로 가서 다시 줄을 섬
    queue.append((new_people, 0))  # 새로운 사람도 줄을 섬

print(last_people)