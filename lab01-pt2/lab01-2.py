'''
CMSC 180 Lab 01 Part 01
Author: Aron Resty Ramillano | 2020-01721
Section: T3L
'''

# We will be using our code from last time and improving it for better output

import random
import math
import time

def row_print(matx):
    """
    It prints the matrix in a nice way
    
    :param matx: the matrix to be printed
    """
    print("Matrix:")
    for row in matx:
        print(row)


def coords_print(matx):
    """
    It prints the coordinates and values of a matrix
    
    :param matx: The matrix to be printed
    """
    print("Matrix Coordinates and Values")
    for i in range(len(matx)):
        for j in range(len(matx[0])):
            print("x: ",i,", y:", j,", val:", matx[i][j])


def create_matx(n):
    """
    It creates an n x n matrix with all zeros
    
    :param n: the number of nodes in the graph
    :return: A matrix of size n+1
    """
    # print("Generating empty matrix...")
    n+=1
    matx = [[0 for i in range(n)] for j in range(n)]
    return matx


def rand_pop_matx(matx):
    """
    It populates the matrix with random elevation values at every 10th index
    
    :param matx: The matrix that will be populated with random elevation values
    """
    # print("Populating Matrix with randomized elevation values...")
    for i in range(len(matx)):
        for j in range(len(matx[0])):
            if (((i)%10 == 0) and ((j)%10 == 0)):
                matx[i][j] = random.randint(1, 1000)


def terrain_inter(M):
    """
    It takes a matrix and for each point in the matrix, it calls a function that interpolates the point
    based on the surrounding points
    
    :param M: The matrix
    """
    for i in range(len(M)):
        min_x, max_x = get_min_max(i)
        for j in range(len(M[0])):
            if not (((i)%10 == 0) and ((j)%10 == 0)):
                min_y, max_y = get_min_max(j)

                # We use the Area Weighted Interpolation
                a_w_point_inter(M,i,j, min_x, max_x, min_y, max_y)


def get_min_max(n):
    """
    It takes a number and returns the minimum and maximum numbers that are multiples of 10 and are
    within 10 of the input number
    
    :param n: The number of elements in the array
    :return: The minimum and maximum values of the range of numbers that the input number belongs to.
    """
    min = math.floor((n-1 if n > 1 else 1)/10)*10
    max = math.ceil((n if n > 0 else 1)/10)*10
    # print("Min:",min,", Max:",max)
    return min, max
       
'''
We removed the get_area and get_elev functions and hardcoded it into our main function which is the a_w_point_inter to cut down on processing power
'''

def a_w_point_inter(matx, x, y, min_x, max_x, min_y, max_y):
    """
    The function takes in a matrix, a point, and the min and max x and y values of the matrix, and then
    calculates the elevation of the point using the weighted average of the elevation of the four points
    surrounding it.
    
    :param matx: The matrix of elevations
    :param x: x-coordinate of the point
    :param y: the y coordinate of the point
    :param min_x: the minimum x value of the square
    :param max_x: the x coordinate of the top right corner of the square
    :param min_y: the minimum y value of the surrounding points
    :param max_y: the maximum y value of the matrix
    """
    area_d, area_c, area_b, area_a = (abs(min_x - x) * abs(min_y - y)), (abs(max_x - x) * abs(min_y - y)), (abs(min_x - x) * abs(max_y - y)), (abs(max_x - x) * abs(max_y - y))
    elev_a, elev_b, elev_c, elev_d = matx[min_x][min_y], matx[max_x][min_y], matx[min_x][max_y], matx[max_x][max_y]
    
    elevation = ((area_a*elev_a) + (area_b*elev_b) + (area_c*elev_c) + (area_d*elev_d)) / (area_a + area_b + area_c + area_d)
    
    # print("Elevation of point(", x,",",y,") =", elevation)
    
    matx[x][y] = elevation
    
# n = 1
# # Get user input
# while n:
#     n = int(input("\nEnter a number divisible by 10: "))
#     if not n%10:
#         matx = create_matx(n)
#         break

# # Generate matrix with randomized values
# rand_pop_matx(matx)

# # Start the function and get the elapsed time
# start = time.time()
# terrain_inter(matx)
# end = time.time()

# choice = int(input("Do you want to print the resulting matrix? [1] if yes, [0] if no: "))
# if choice == 1:
#     row_print(matx)
    
# print("Time Elapsed:",end - start, "seconds")

def run_main(n):
    print("Matrix size:", n, end=" | ")
    matx = create_matx(n)
    rand_pop_matx(matx)
    start = time.time()
    terrain_inter(matx)
    end = time.time()
    print("Time Elapsed:",end - start, "seconds")

for i in range(0, 3):
    print("Run #", i+1, ":")
    run_main(100)
    run_main(200)
    run_main(300)
    run_main(400)
    run_main(500)
    run_main(600)
    run_main(700)
    run_main(800)
    run_main(900)
    run_main(1000)
    run_main(2000)
    run_main(3000)
    run_main(4000)
    run_main(8000)
    run_main(16000)
    run_main(20000)