# epsilon-net of size 3 for square, points are randomly placed in the grid


import random

# given a list of integers, a number n, find the duration <= n, such that number of points in that duration from the list is maximum and return the count in that duration.

def findMaxSquare(lst, arm):
    # sort the list in ascending order
    lst.sort()

    # if no element in the list return 0 or if arm length is nil return 0
    if not lst or (arm < 1):
        return 0

    # now take two pointer approach, one pointer will hold the address of left most elements under consideration and another pointer will keep proceeding right until the duration
    # goes beyond the length of arm.

    i = j = 0
    max = 0
    # iterate over all the elements in the list
    while j < len(lst):
        # arm is length of the arm of square, difference between two points must be less than the length of arm
        if lst[j] - lst[i] < arm:
            j += 1
        else:
            if (j - i) > max:
                max = j - i
            i += 1

    if (j - i) > max:
        max = j - i

    return max



def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

def findMax(lst):
    max = lst[0]
    for item in lst:
        if item > max:
            max = item
    return max


def plotBestResultPoints(bestResultPoints):
    x = []
    y = []
    for i in range(0, len(bestResultPoints)):
        for j in range(0, len(bestResultPoints[i][0])):
            x.append(bestResultPoints[i][0][j][0])
            y.append(bestResultPoints[i][0][j][1])
            plt.figure(i)
            plt.scatter(x, y)
        x = []
        y = []
    plt.show()
# for N different distributions of points we will check the fraction


N = int(input())
best_result = 0
best_result_points = []

return_count = 0

def main_algo(points, N):
    # points = [[2, 3], [3, 5], [5, 2], [6, 4], [3, 2], [5, 6]]
    # initial value of result is very high
    min_of_maxes = 999999999999
    # for every pair of points we need max
    max = 0
    # iterate over every pair of points
    for j in range(0, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                x1 = points[j][0]
                y1 = points[j][1]
                x2 = points[k][0]
                y2 = points[k][1]
                x3 = points[l][0]
                y3 = points[l][1]
                # this is 1st case of choosen points
                # x1 < x2 < x3 for each pointset, as those are generated such a way only
                if y2 > y1 and y3 > y2:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy3 = y2LyLy3 = y1LyLy2 = yLy1 = xLx3AyGy2 = xLx2AyGy1 = xGx2AyLy3 = xGx1AyLy2 = 0

                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y2LyLy3listOnlyXaxs = []
                    y1LyLy2listOnlyXaxs = []

                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 12 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y3:
                            yGy3 += 1
                        if currenty < y3 and currenty > y2:
                            y2LyLy3listOnlyXaxs.append(currentx)
                        if currenty < y2 and currenty > y1:
                            y1LyLy2listOnlyXaxs.append(currentx)
                        if currenty < y1:
                            yLy1 += 1
                        if currentx < x3 and currenty > y2:
                            xLx3AyGy2 += 1
                        if currentx < x2 and currenty > y1:
                            xLx2AyGy1 += 1
                        if currentx > x2 and currenty < y3:
                            xGx2AyLy3 += 1
                        if currentx > x1 and currenty < y2:
                            xGx1AyLy2 += 1

                    '''now find the values for complicated squares'''
                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y2LyLy3 = findMaxSquare(y2LyLy3listOnlyXaxs, abs(y2 - y3))
                    y1LyLy2 = findMaxSquare(y1LyLy2listOnlyXaxs, abs(y1 - y2))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy3, y2LyLy3, y1LyLy2, yLy1, xLx3AyGy2, xLx2AyGy1, xGx2AyLy3, xGx1AyLy2]
                    max = findMax(regions)

                # case 2
                if y3 > y1 and y2 > y3:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy2 = y3LyLy2 = y1LyLy3 = yLy1 = y1LyLy2AxLx3 = x1LxLx3AyLy2 = xLx2AyGy1 = xGx2AyGy3 = xGx1AyLy3 = 0
                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y3LyLy2listOnlyXaxs = []
                    y1LyLy3listOnlyXaxs = []
                    y1LyLy2AxLx3listOnlyXaxs = []
                    x1LxLx3AyLy2listOnlyYaxs = []
                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 13 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y2:
                            yGy2 += 1
                        if currenty < y2 and currenty > y3:
                            y3LyLy2listOnlyXaxs.append(currentx)
                        if currenty < y3 and currenty > y1:
                            y1LyLy3listOnlyXaxs.append(currentx)
                        if currenty < y1:
                            yLy1 += 1
                        if currenty < y2 and currenty > y1 and currentx < x3:
                            y1LyLy2AxLx3listOnlyXaxs.append(currentx)
                        if currentx > x1 and currentx < x3 and currenty < y2:
                            x1LxLx3AyLy2listOnlyYaxs.append(currenty)
                        if currentx < x2 and currenty > y1:
                            xLx2AyGy1 += 1
                        if currentx > x2 and currenty > y3:
                            xGx2AyGy3 += 1
                        if currentx > x1 and currenty < y3:
                            xGx1AyLy3 += 1

                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y3LyLy2 = findMaxSquare(y3LyLy2listOnlyXaxs, abs(y3 - y2))
                    y1LyLy3 = findMaxSquare(y1LyLy3listOnlyXaxs, abs(y1 - y3))
                    y1LyLy2AxLx3 = findMaxSquare(y1LyLy2AxLx3listOnlyXaxs, abs(y1 - y2))
                    x1LxLx3AyLy2 = findMaxSquare(x1LxLx3AyLy2listOnlyYaxs, abs(x1 - x3))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy2, y3LyLy2, y1LyLy3, yLy1, y1LyLy2AxLx3, x1LxLx3AyLy2,
                               xLx2AyGy1, xGx2AyGy3, xGx1AyLy3]
                    max = findMax(regions)

                # case 3
                if y1 > y2 and y3 > y1:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy3 = y1LyLy3 = y2LyLy1 = yLy2 = xGx1Ay2LyLy3 = yGy2Ax1LxLx3 = xLx2AyLy1 = xLx3AyGy1 = xGx2AyLy3 = 0
                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y1LyLy3listOnlyXaxs = []
                    y2LyLy1listOnlyXaxs = []
                    xGx1Ay2LyLy3listOnlyXaxs = []
                    yGy2Ax1LxLx3listOnlyYaxs = []
                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 13 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y3:
                            yGy3 += 1
                        if currenty < y3 and currenty > y1:
                            y1LyLy3listOnlyXaxs.append(currentx)
                        if currenty < y1 and currenty > y2:
                            y2LyLy1listOnlyXaxs.append(currentx)
                        if currenty < y2:
                            yLy2 += 1
                        if currentx > x1 and currenty > y2 and currenty < y3:
                            xGx1Ay2LyLy3listOnlyXaxs.append(currentx)
                        if currenty > y2 and currentx < x3 and currentx > x1:
                            yGy2Ax1LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currenty < y1:
                            xLx2AyLy1 += 1
                        if currentx < x3 and currenty > y1:
                            xLx3AyGy1 += 1
                        if currentx > x2 and currenty < y3:
                            xGx2AyLy3 += 1

                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y1LyLy3 = findMaxSquare(y1LyLy3listOnlyXaxs, abs(y1 - y3))
                    y2LyLy1 = findMaxSquare(y2LyLy1listOnlyXaxs, abs(y1 - y2))
                    xGx1Ay2LyLy3 = findMaxSquare(xGx1Ay2LyLy3listOnlyXaxs, abs(y2 - y3))
                    yGy2Ax1LxLx3 = findMaxSquare(yGy2Ax1LxLx3listOnlyYaxs, abs(x1 - x3))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy3, y1LyLy3, y2LyLy1, yLy2, xGx1Ay2LyLy3, yGy2Ax1LxLx3,
                               xLx2AyLy1, xLx3AyGy1, xGx2AyLy3]
                    max = findMax(regions)

                # case 4
                if y3 > y2 and y1 > y3:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy1 = y3LyLy1 = y2LyLy3 = yLy2 = xLx3Ay2LyLy1 = yGy2Ax1LxLx3 = xGx1AyGy3 = xLx2AyLy1 = xGx2AyLy3 = 0
                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y3LyLy1listOnlyXaxs = []
                    y2LyLy3listOnlyXaxs = []
                    xLx3Ay2LyLy1listOnlyXaxs = []
                    yGy2Ax1LxLx3listOnlyYaxs = []
                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 13 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y1:
                            yGy1 += 1
                        if currenty < y1 and currenty > y3:
                            y3LyLy1listOnlyXaxs.append(currentx)
                        if currenty < y3 and currenty > y2:
                            y2LyLy3listOnlyXaxs.append(currentx)
                        if currenty < y2:
                            yLy2 += 1
                        if currentx < x3 and currenty > y2 and currenty < y1:
                            xLx3Ay2LyLy1listOnlyXaxs.append(currentx)
                        if currenty > y2 and currentx < x3 and currentx > x1:
                            yGy2Ax1LxLx3listOnlyYaxs.append(currentx)
                        if currentx > x1 and currenty > y3:
                            xGx1AyGy3 += 1
                        if currentx < x2 and currenty < y1:
                            xLx2AyLy1 += 1
                        if currentx > x2 and currenty < y3:
                            xGx2AyLy3 += 1

                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y3LyLy1 = findMaxSquare(y3LyLy1listOnlyXaxs, abs(y1 - y3))
                    y2LyLy3 = findMaxSquare(y2LyLy3listOnlyXaxs, abs(y2 - y3))
                    xLx3Ay2LyLy1 = findMaxSquare(xLx3Ay2LyLy1listOnlyXaxs, abs(y1 - y2))
                    yGy2Ax1LxLx3 = findMaxSquare(yGy2Ax1LxLx3listOnlyYaxs, abs(x1 - x3))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy1, y3LyLy1, y2LyLy3, yLy2, xLx3Ay2LyLy1, yGy2Ax1LxLx3,
                               xGx1AyGy3, xLx2AyLy1, xGx2AyLy3]
                    max = findMax(regions)

                # case 5
                if y2 > y1 and y1 > y3:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy2 = y1LyLy2 = y3LyLy1 = yLy3 = xGx1Ay3LyLy2 = yLy2Ax1LxLx3 = xLx2AyGy1 = xLx3AyLy1 = xGx2AyGy3 = 0
                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y1LyLy2listOnlyXaxs = []
                    y3LyLy1listOnlyXaxs = []
                    xGx1Ay3LyLy2listOnlyXaxs = []
                    yLy2Ax1LxLx3listOnlyYaxs = []
                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 13 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y2:
                            yGy2 += 1
                        if currenty < y2 and currenty > y1:
                            y1LyLy2listOnlyXaxs.append(currentx)
                        if currenty < y1 and currenty > y3:
                            y3LyLy1listOnlyXaxs.append(currentx)
                        if currenty < y3:
                            yLy3 += 1
                        if currentx > x1 and currenty < y2 and currenty > y3:
                            xGx1Ay3LyLy2listOnlyXaxs.append(currentx)
                        if currenty < y2 and currentx < x3 and currentx > x1:
                            yLy2Ax1LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currenty > y1:
                            xLx2AyGy1 += 1
                        if currentx < x3 and currenty < y1:
                            xLx3AyLy1 += 1
                        if currentx > x2 and currenty > y3:
                            xGx2AyGy3 += 1

                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y1LyLy2 = findMaxSquare(y1LyLy2listOnlyXaxs, abs(y1 - y2))
                    y3LyLy1 = findMaxSquare(y3LyLy1listOnlyXaxs, abs(y3 - y1))
                    xGx1Ay3LyLy2 = findMaxSquare(xGx1Ay3LyLy2listOnlyXaxs, abs(y2 - y3))
                    yLy2Ax1LxLx3 = findMaxSquare(yLy2Ax1LxLx3listOnlyYaxs, abs(x1 - x3))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy2, y1LyLy2, y3LyLy1, yLy3, xGx1Ay3LyLy2, yLy2Ax1LxLx3,
                               xLx2AyGy1, xLx3AyLy1, xGx2AyGy3]
                    max = findMax(regions)

                # case 6
                if y1 > y2 and y2 > y3:
                    # initialize every region count to 0
                    xGx3 = x2LxLx3 = x1LxLx2 = xLx1 = yGy1 = y2LyLy1 = y3LyLy2 = yLy3 = xLx2AyLy1 = xLx3AyLy2 = xGx1AyGy2 = xGx2AyGy3 = 0
                    x2LxLx3listOnlyYaxs = []
                    x1LxLx2listOnlyYaxs = []
                    y2LyLy1listOnlyXaxs = []
                    y3LyLy2listOnlyXaxs = []
                    # go through all the points
                    for m in range(0, N):
                        # if current point matches to the points pair then continue
                        if m == j or m == k or m == l:
                            continue
                        currentx = points[m][0]
                        currenty = points[m][1]

                        # these are corresponding to all the condition of 12 regions
                        if currentx > x3:
                            xGx3 += 1
                        if currentx < x3 and currentx > x2:
                            x2LxLx3listOnlyYaxs.append(currenty)
                        if currentx < x2 and currentx > x1:
                            x1LxLx2listOnlyYaxs.append(currenty)
                        if currentx < x1:
                            xLx1 += 1
                        if currenty > y1:
                            yGy1 += 1
                        if currenty < y1 and currenty > y2:
                            y2LyLy1listOnlyXaxs.append(currentx)
                        if currenty < y2 and currenty > y3:
                            y3LyLy2listOnlyXaxs.append(currentx)
                        if currenty < y3:
                            yLy3 += 1
                        if currentx < x2 and currenty < y1:
                            xLx2AyLy1 += 1
                        if currentx < x3 and currenty < y2:
                            xLx3AyLy2 += 1
                        if currentx > x1 and currenty > y2:
                            xGx1AyGy2 += 1
                        if currentx > x2 and currenty > y3:
                            xGx2AyGy3 += 1

                    x2LxLx3 = findMaxSquare(x2LxLx3listOnlyYaxs, abs(x2 - x3))
                    x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                    y2LyLy1 = findMaxSquare(y2LyLy1listOnlyXaxs, abs(y1 - y2))
                    y3LyLy2 = findMaxSquare(y3LyLy2listOnlyXaxs, abs(y3 - y2))
                    # now found out the region containing maximum number of points
                    regions = [xGx3, x2LxLx3, x1LxLx2, xLx1, yGy1, y2LyLy1, y3LyLy2, yLy3, xLx2AyLy1, xLx3AyLy2,
                               xGx1AyGy2, xGx2AyGy3]
                    max = findMax(regions)

                # max less than result update max
                # print(max, "****")
                if max < min_of_maxes:
                    min_of_maxes = max
    # print(min_of_maxes / N)
    global best_result
    global best_result_points
    if best_result < (min_of_maxes / N):
        best_result_points = []
        best_result = (min_of_maxes / N)
        pointPlusFrac = [points, best_result]
        print(pointPlusFrac)
        # best_result_points.append(pointPlusFrac)
    '''elif best_result == (min_of_maxes / N):
        pointPlusFrac = [points, best_result]
        best_result_points.append(pointPlusFrac)'''


def generate_permutations_and_call_algo(arr, l, r):
    if l == r:
        point_set = []
        for i in range(0, N):
            point_set.append([i, arr[i]])
        # print(point_set)
        main_algo(point_set, N)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            generate_permutations_and_call_algo(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]  # backtrack



grid_size = N
while True:
    # X = [x for x in range(0, N)]
    Y = [y for y in range(0, N)]
    point_set = []
    for i in range(0, N):
        point_set.append([i, Y.pop(random.randint(0, len(Y) - 1))])
    # print(point_set)
    main_algo(point_set, N)