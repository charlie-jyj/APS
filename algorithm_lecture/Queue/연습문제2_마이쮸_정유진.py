my_queue = [0]*30
front = rear = -1

candy = 20
human = 0

while candy>0:

    # 사람이 줄을 선다.
    human += 1
    rear += 1
    my_queue[rear] = [human, 1]  # [사람 번호, 받을 사탕 수]
    print('현재까지 나눠준 마이쮸의 수:', 20-candy, '줄 서 있는 사람 수:', rear - front, my_queue[front+1:rear+1])

    # 줄의 첫 번째 사람을 확인한다
    front += 1
    first = my_queue[front]
    print('이번에 받을 사람:', first[0], ', 받을 마이쮸의 수:', first[1])

    if candy - first[1] <= 0:
        print('마지막 마이쮸를 받을 사람은? ', first[0], '번')
        break

    # 마이쮸를 준다.
    candy -= first[1]

    # 마이쮸를 받고 다시 줄을 선다.
    first[1] += 1  # 다음에 받을 사탕 개수 1개 증가
    rear += 1
    my_queue[rear] = first

