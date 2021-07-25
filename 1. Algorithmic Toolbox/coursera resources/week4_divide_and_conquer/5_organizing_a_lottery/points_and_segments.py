# Uses python3
import sys
import datetime

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    time1 = datetime.datetime.now()
    cnt = naive_count_segments(starts, ends, points)
    time2 = datetime.datetime.now()
    print((time2 - time1).microseconds / 1000)
    for x in cnt:
        print(x, end=' ')
