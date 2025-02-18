# da01_queue.py
# 큐 자료구조 구현

# 2. 함수 선언 > 선언만 해서 메모리에만 입력되어서 사용자는 못봄

def isQueueFull():
    global SIZE, queue, front, rear
    # 1. 가장 일잔적인 로직
    # if rear == SIZE - 1:
    #     return True
    # else:
    #     return False
    # 2. 개선 로직 > 비어있는 None칸에 다시 넣을수 있게 바꿈 
    if rear != SIZE - 1:
        return False
    elif rear == SIZE - 1 and front == -1 :
        return True
    else:                 # p253 페이지 보기 
        for i in range(front+1 , SIZE):
            queue[i-1] = queue[i] # 데이터앞 빈자리에 첫번째 데이터 옮김
            queue[i] = None

        front -= 1
        rear -= 1
        return False

    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueu(data): # enQueue 에 집어넣을 싸이즈(data)를 넣음
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full')
    else:
        rear += 1
        queue[rear] = data

def deQueue(): # deQueue 는 빼는거 
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None  # 리턴 None 왜 한지 보기 
    else: # 이 로직 뭔지 보기 
        front += 1
        data = queue[front]
        queue[front] = None
        return data
    
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[front+1]

# 1.초기화
SIZE = int(input('큐 크기 입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = -1

## 3.메인 모듈
if __name__=='__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) -->').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueu(data) # enQueue는 엔터 큐 데이터 넣기 
            print(f'큐 상태 : {queue}')
        elif select == 'E':
            data =deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태: {queue}')
        elif select == 'V':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태: {queue}')

        else:
            print('입력 오류')