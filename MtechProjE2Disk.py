from math import sqrt
import numpy as np
import random
import matplotlib.pyplot as plt


class circle:
    centre = []
    radius = 0
    point_count = 0
    status = "dontconsider"

# this function will take center and radius of a circle and a point. will return if the point is on the circle or inside or outside.
def locPointWrtCircle(point, circle):
    px = point[0]
    py = point[1]
    cx = circle.centre[0]
    cy = circle.centre[1]

    dist = round(sqrt((cx - px) ** 2 + (cy - py) ** 2), 4)
    # print("distance of point ",point, "from centre = ", dist)
    if dist == circle.radius:
        return "on"
    elif dist < circle.radius:
        return "inside"
    else:
        return "outside"


def collinear(x1, y1, x2, y2, x3, y3):
    """ Calculation the area of
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if (a == 0):
        return("yes")
    else:
        return("no")


# given 3 points it will return the radius and center of the unique circle possible.
def findCircleGiven3Points(points):
    #print("\n", points)
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]
    x3 = points[2][0]
    y3 = points[2][1]

    A = np.array([[2 * x1, 2 * y1, 1], [2 * x2, 2 * y2, 1], [2 * x3, 2 * y3, 1]])
    B = np.array([-(x1 ** 2 + y1 ** 2), -(x2 ** 2 + y2 ** 2), -(x3 ** 2 + y3 ** 2)])
    #print(A, B)
    X = np.linalg.inv(A).dot(B)

    g = X[0]
    f = X[1]
    c = X[2]
    # print("-g, -f, c = ",-g, -f, c)

    #print(g ** 2 + f ** 2 - c)
    radius = round(sqrt(g ** 2 + f ** 2 - c), 4)
    #print(radius)
    centre = [-g, -f]

    cir = circle()
    cir.centre = centre
    cir.radius = radius

    return cir


def findMax(lst):
    max = lst[0][0][0].point_count
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            for item in lst[i][j]:
                if item.point_count > max:
                    max = item.point_count
        return max


N = int(input())
best_result = 0
best_result_points = []
# findCircleGiven3Points([[1, 2], [20, 3], [11, 6]])

def main_algo(points, N):
    # points = [[2, 3], [3, 5], [5, 2], [6, 4], [3, 2], [5, 6]]
    # initial value of result is very high
    min_of_maxes = 999999999999
    # iterate over every pair of points (epsilon points)
    # print("********************************************************\npointset =", points)
    '''count = 0
    figure, axes = plt.subplots()
    axes.set_aspect(1)'''
    for j in range(0, N):
        for k in range(j + 1, N):
            # print("----------------\nepsilon-net points = ",points[j], points[k])
            # initialize every halfspcLine count to 0 also default orientation
            regions = [[[circle() for l in range(0, N)] for m in range(0, N)] for o in range(0, N)]
            # update the orientation of each halfspace either left or right or both or DontConsider, (a, b) halfspace line points
            for a in range(0, N):
                for b in range(a + 1, N):
                    for c in range(b + 1, N):
                        circlePoints = [points[a], points[b], points[c]]
                        if collinear(points[a][0], points[a][1], points[b][0], points[b][1], points[c][0], points[c][1]) == "no":
                            regions[a][b][c] = findCircleGiven3Points(circlePoints)
                            # print("radius = ", regions[a][b][c].radius)
                            '''concurrentCircle = regions[a][b][c]
                            if count == 0:
                                axes.add_artist(plt.Circle((concurrentCircle.centre[0], concurrentCircle.centre[1]),
                                                           concurrentCircle.radius,
                                                           fill=False))'''

                            '''if locPointWrtCircle(points[j], regions[a][b][c]) == "outside" and locPointWrtCircle(points[k], regions[a][b][c]) == "outside":
                                regions[a][b][c].status = "consider"'''
                            if locPointWrtCircle(points[j], regions[a][b][c]) != "inside" and locPointWrtCircle(points[k], regions[a][b][c]) != "inside":
                                regions[a][b][c].status = "consider"
            # count = 1
            # print(points[j], points[k])
            # go through all the points
            for q in range(0, N):
                # if current point matches to the epsilon net points pair then continue
                if q == j or q == k:
                    continue

                # go through all the regions and check if the current point orientation matches with the current halfspcLine orientation or not, if match increment.
                for a in range(0, N):
                    for b in range(a + 1, N):
                        for c in range(b + 1, N):

                            if regions[a][b][c].status != "dontconsider":
                                locOfPoint = locPointWrtCircle(points[q], regions[a][b][c])
                                if regions[a][b][c].status == "consider":
                                    if locOfPoint != "outside":
                                        regions[a][b][c].point_count += 1
                                '''elif regions[a][b][c].status == "consideronlyinside":
                                    if locOfPoint == "inside":
                                        regions[a][b][c].point_count += 1'''

            # print("\n", points[j], points[k])
            '''for a in range(0, N):
                for b in range(a + 1, N):
                    for c in range(b + 1, N):
                        print("circle = ", points[a], points[b], points[c], ", status = ", regions[a][b][c].status, ", number of points =", regions[a][b][c].point_count)'''



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

    '''plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.yticks(np.arange(-10, 10, 2))
    plt.xticks(np.arange(-10, 10, 2))

    x = []
    y = []
    for i in range(0, N):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y, 'o', color = 'red')

    plt.show()'''


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
generate_permutations_and_call_algo(arr, 0, N - 1)'''

# main_algo([[0, 0], [0, 8], [2, 0], [2, 7]], 4)


grid_size = 1000
while True:
    point_set = []
    for i in range(0, N):
        point_set.append([random.randint(0, grid_size), random.randint(0, grid_size)])
    main_algo(point_set, N)

'''print("Best result = ", best_result)
print("best result points = ", best_result_points)'''
