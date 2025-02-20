# 성적별로 조 편성하기 

def scorSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1][1] > ary[cur][1]):  # 이거 이해안감
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

# 전역 변수 선언 부분
scorAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

# 메인코드 부분
print('정렬 전 -->', scorAry)
scorAry = scorSort(scorAry)
print('정렬 후 -->', scorAry)
print('## 성적별 조 편성표')
for i in range(len(scorAry)//2):
    print(scorAry[i][0],':', scorAry[len(scorAry)-1-i][0])