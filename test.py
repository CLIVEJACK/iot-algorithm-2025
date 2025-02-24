import random
count = 0
def binSearch(ary,data):
    global count
    pos = -1 
    start = 0
    end = len(ary) - 1

    while(start <= end):
        mid = (start + end) // 2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1 
        else:
            end = mid - 1
            count += 1
            
# 전역변수 
dataAry = range(0, 10000)
findData = random.choice(dataAry)

# 메인 

print('배열-->',dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(f'{findData} 는 없네요.')
else: 
    print(f'{findData} 는 {position} 위에있음')

print(f'{count}회 검색함')
