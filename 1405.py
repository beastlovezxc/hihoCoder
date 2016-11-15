import sys

while True:
    try:
        INF = 9999999
        maxn = 105

        def func(left, right):
            if left > right:
                return
            if left == right:
                print num[left],
                return
            minVal = INF
            minp = -1

            for i in range(left, right+1):
                if minVal > num[i]:
                    minVal = num[i]
                    minp = i
            print num[minp],
            func(left, minp - 1)
            func(minp + 1, right)

        n = int(raw_input())
        num = map(int, sys.stdin.readline().split())
        
        # print num
        # n = 6
        # num = [3, 2, 8, 1, 4, 7]
        func(0, n - 1)
    except EOFError:
        break
