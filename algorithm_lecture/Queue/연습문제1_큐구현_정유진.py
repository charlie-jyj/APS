# 선형 큐 (배열)
class MyQueue():

    def __init__(self, n):
        self.queue = [0] * n  # 크기 지정
        self.front = self. rear = -1  # 초기 상태

    def is_full(self):
        return self.rear == len(self.queue)-1  # rear가 배열의 끝 인덱스 일때,

    def is_empty(self):
        return self.front == self.rear  # front 와 rear 가 같을 때

    def en_queue(self, item):

        if self.is_full():
            print('Queue is full')
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def de_queue(self):

        if self.is_empty():
            print('Queue is empty')
        else:
            self.front += 1
            return self.queue[self.front]

    def peek(self):

        if self.is_empty():
            print('Queue is empty')
        else:
            return self.queue[self.front+1]

    def __str__(self):
        return str(self.queue[self.front+1:self.rear+1])


q = MyQueue(5)
q.en_queue(1)
q.en_queue(2)
q.en_queue(3)
print(q)


# 리스트 큐
class MyQueueList():

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def en_queue(self, item):

        self.queue.append(item)

    def de_queue(self):

        if self.is_empty():
            print('Queue is empty')
        else:
            return self.queue.pop(0)

    def peek(self):

        if self.is_empty():
            print('Queue is empty')
        else:
            return self.queue[0]

    def __str__(self):
        return str(self.queue)


q2 = MyQueueList()
q2.en_queue(1)
q2.en_queue(2)
q2.en_queue(3)
print(q2)