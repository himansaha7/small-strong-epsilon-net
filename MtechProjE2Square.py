# epsilon-net of size 2 for square


# It is not completely same as axis parallel rectangles, because in the middle of two epsilon net points the arm length of square can not be more than the distance between two epsilon
# net points.
'''as there are two cases for axis parallel rectangle, all the condition of those cases are same as axis parallel square only difference is in middle condition, for all other condi
tions as length and breadth of the square is open we can extend the square as much as we want, which will include all the points we were able to include in case of axis parallel recta
ngles.'''


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


'''the change will be like I have to collect all the points falling inside that considerable region and pass to our function above to get maximum possible square containing maxim
 um number of points from that point set.'''


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
            x1 = points[j][0]
            y1 = points[j][1]
            x2 = points[k][0]
            y2 = points[k][1]
            # this is 1st case of choosen points
            if x2 > x1 and y2 > y1:
                # initialize every region count to 0
                yGy2 = yLy1 = xLx1 = xGx2 = x1LxLx2 = y1LyLy2 = xGx1AyLy2 = yGy1AxLx2 = 0
                x1LxLx2listOnlyYaxs = []
                y1LyLy2listOnlyXaxs = []
                # go through all the points
                for l in range(0, N):
                    # if current point matches to the points pair then continue
                    if l == j or l == k:
                        continue
                    currentx = points[l][0]
                    currenty = points[l][1]

                    # these are corresponding to all the condition of 8 regions
                    if currenty > y2:
                        yGy2 += 1
                    elif currenty < y1:
                        yLy1 += 1
                    if currentx < x1:
                        xLx1 += 1
                    elif currentx > x2:
                        xGx2 += 1
                    if currentx > x1 and currentx < x2:
                        x1LxLx2listOnlyYaxs.append(currenty)
                    if currenty > y1 and currenty < y2:
                        y1LyLy2listOnlyXaxs.append(currentx)
                    if currentx > x1 and currenty < y2:
                        xGx1AyLy2 += 1
                    if currenty > y1 and currentx < x2:
                        yGy1AxLx2 += 1

                '''now find the values for x1LxLx2 and y1LyLy2'''
                x1LxLx2 = findMaxSquare(x1LxLx2listOnlyYaxs, abs(x1 - x2))
                y1LyLy2 = findMaxSquare(y1LyLy2listOnlyXaxs, abs(y1 - y2))
                # now found out the region containing maximum number of points
                max = yGy2
                if yLy1 > max:
                    max = yLy1
                if xLx1 > max:
                    max = xLx1
                if xGx2 > max:
                    max = xGx2
                if x1LxLx2 > max:
                    max = x1LxLx2
                if y1LyLy2 > max:
                    max = y1LyLy2
                if xGx1AyLy2 > max:
                    max = xGx1AyLy2
                if yGy1AxLx2 > max:
                    max = yGy1AxLx2

            # this is 2nd case of choosen points
            if x2 > x1 and y2 < y1:
                yGy1 = yLy2 = xLx1 = xGx2 = x2LxLx1 = y2LyLy1 = xLx2AyLy1 = xGx1AyGy2 = 0
                x2LxLx1listOnlyYaxs = []
                y2LyLy1listOnlyXaxs = []
                # go through all the points
                for l in range(0, N):
                    # if current point matches to the points pair then continue
                    if l == j or l == k:
                        continue
                    currentx = points[l][0]
                    currenty = points[l][1]

                    # these are corresponding to all the condition of 8 regions
                    if currenty > y1:
                        yGy1 += 1
                    elif currenty < y2:
                        yLy2 += 1
                    if currentx < x1:
                        xLx1 += 1
                    elif currentx > x2:
                        xGx2 += 1
                    if currentx > x2 and currentx < x1:
                        x2LxLx1listOnlyYaxs.append(currenty)
                    if currenty > y2 and currenty < y1:
                        y2LyLy1listOnlyXaxs.append(currentx)
                    if currentx < x2 and currenty < y1:
                        xLx2AyLy1 += 1
                    if currenty > y2 and currentx > x1:
                        xGx1AyGy2 += 1

                '''now find the values for x2LxLx1 and y2LyLy1'''
                x2LxLx1 = findMaxSquare(x2LxLx1listOnlyYaxs, abs(x1 - x2))
                y2LyLy1 = findMaxSquare(y2LyLy1listOnlyXaxs, abs(y1 - y2))
                # now found out the region containing maximum number of points
                max = yGy1
                if yLy2 > max:
                    max = yLy2
                if xLx1 > max:
                    max = xLx1
                if xGx2 > max:
                    max = xGx2
                if x2LxLx1 > max:
                    max = x2LxLx1
                if y2LyLy1 > max:
                    max = y2LyLy1
                if xLx2AyLy1 > max:
                    max = xLx2AyLy1
                if xGx1AyGy2 > max:
                    max = xGx1AyGy2
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



arr = []
for i in range(0, N):
    arr.append(i)
generate_permutations_and_call_algo(arr, 0, N - 1)


'''print("Best result = ", best_result)
print("best result points = ")
for item in best_result_points:
    print(item)'''

# plotBestResultPoints(best_result_points)