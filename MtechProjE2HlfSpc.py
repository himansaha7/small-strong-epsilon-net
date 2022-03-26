
import random

def swap(a, b):
    return (b, a)


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

class halfspcLine:
    left_count = 0
    right_count = 0
    orientation = "DontConsider"


def findMax(lst):
    max = lst[0][0].left_count
    for i in range(0, len(lst)):
        for item in lst[i]:
            if item.right_count > max:
                max = item.right_count
            if item.left_count > max:
                max = item.left_count
    return max



def directionOfPoint(A, B, P):

    # Subtracting co-ordinates of
    # point A from B and P, to
    # make A as origin
    Ax = A[0]
    Ay = A[1]
    Bx = B[0]
    By = B[1]
    Px = P[0]
    Py = P[1]


    Bx -= Ax
    By -= Ay
    Px -= Ax
    Py -= Ay


    # Determining cross Product
    cross_product = Bx * Py - By * Px


    # Return RIGHT if cross product is positive
    if (cross_product > 0):
        return "left"

    # Return LEFT if cross product is negative
    if (cross_product < 0):
        return "right"

    # Return ZERO if cross product is zero
    return "zero"

# for N different distributions of points we will check the fraction


N = int(input())
best_result = 0
best_result_points = []

return_count = 0

def main_algo(points, N):
    # points = [[2, 3], [3, 5], [5, 2], [6, 4], [3, 2], [5, 6]]
    # initial value of result is very high
    min_of_maxes = 999999999999
    # iterate over every pair of points (epsilon points)
    # print("\n", points, "\n")
    for j in range(0, N):
        for k in range(j + 1, N):
            # initialize every halfspcLine count to 0 also default orientation
            regions = [[halfspcLine() for l in range(0, N)] for m in range(0, N)]
            # update the orientation of each halfspace either left or right or both or DontConsider, (a, b) halfspace line points
            for a in range(0, N):
                for b in range(a + 1, N):
                    # if both the epsilon points are on the same side of the halfspace line or over the halfspace line, then assign opposite side, else don't consider
                    # now the funda is when halfspace line contains both the points then we have to take both the sides of halfspace line as valid
                    # halfspaces but how to implement that is now our question.

                    ''' 1) here I have missed one scenario when halfspace line contains points which are not part of epsilon net points and that halfspace line has valid 
                    halfspace region at one of its side then we must include the points on the halfspace line to that region's count.'''
                    if directionOfPoint(points[a], points[b], points[j]) == "zero" and directionOfPoint(points[a], points[b], points[k]) == "zero":
                        regions[a][b].orientation = "both"
                    elif directionOfPoint(points[a], points[b], points[j]) != "left" and directionOfPoint(points[a], points[b], points[k]) != "left":
                        regions[a][b].orientation = "left"
                    elif directionOfPoint(points[a], points[b], points[j]) != "right" and directionOfPoint(points[a], points[b], points[k]) != "right":
                        regions[a][b].orientation = "right"
            # print(points[j], points[k])
            # go through all the points
            for c in range(0, N):
                # if current point matches to the points pair then continue
                if c == j or c == k:
                    continue

                # go through all the regions and check if the current point orientation matches with the current halfspcLine orientation or not, if match increment.
                for a in range(0, N):
                    for b in range(a + 1, N):
                        '''# this is the case when our epsilon net points are lying on the half space line itself
                        if a == j and b == k:
                            regions[a][b].right_count += 1
                            regions[a][b].left_count += 1
                        elif directionOfPoint(points[a], points[b], points[c]) == regions[a][b].orientation:
                            if regions[a][b].orientation == "left":
                                regions[a][b].left_count += 1
                            else:
                                regions[a][b].left_count += 1'''
                        dirOfCurrPoint = directionOfPoint(points[a], points[b], points[c])
                        if regions[a][b].orientation == "both":
                            if dirOfCurrPoint == "left":
                                regions[a][b].left_count += 1
                            elif dirOfCurrPoint == "right":
                                regions[a][b].right_count += 1
                        elif regions[a][b].orientation == "left":
                            if dirOfCurrPoint == "left":
                                regions[a][b].left_count += 1
                        elif regions[a][b].orientation == "right":
                            if dirOfCurrPoint == "right":
                                regions[a][b].right_count += 1

            # implementing point 1)
            for a in range(0, N):
                for b in range(a + 1, N):
                    if directionOfPoint(points[a], points[b], points[j]) != "zero" and directionOfPoint(points[a], points[b], points[k]) != "zero":
                        if regions[a][b].orientation == "left":
                            regions[a][b].left_count += 2
                        elif regions[a][b].orientation == "right":
                            regions[a][b].right_count += 2

            '''print("\n", points[j], points[k])
            for a in range(0, N):
                for b in range(a + 1, N):
                    print(points[a], points[b], regions[a][b].orientation, regions[a][b].left_count, regions[a][b].right_count)'''



            '''for a in range(0, N):
                for b in range(a + 1, N):
                    print(points[a], points[b], "[%d, %d, %s]" % (regions[a][b].left_count, regions[a][b].right_count, regions[a][b].orientation)
                          , directionOfPoint(points[a], points[b], points[j]), directionOfPoint(points[a], points[b], points[k]))'''

            # now found out the halfspcLine containing maximum number of points
            max = findMax(regions)
            # print("max = ", max)

            # max less than min_of_maxes update max
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


'''def generate_permutations_and_call_algo(arr, l, r):
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

main_algo([[-1.294, -4.829], [0, -5], [1.294, -4.829], [0, -1000], [0, -1050]], 5)


print("Best result = ", best_result)
print("best result points = ", best_result_points)'''

grid_size = 1000
while True:
    point_set = []
    for i in range(0, N):
        point_set.append([random.randint(0, grid_size), random.randint(0, grid_size)])
    main_algo(point_set, N)




