// CMSC 180 Lab 01 Part 01
// Author: Aron Resty Ramillano | 2020-01721
// Section: T3L

// This is an attempt to optimize my python code and turn it into C code that is much faster

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

// Resources:
// https://www.geeksforgeeks.org/multidimensional-arrays-c-cpp/
// https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/
// https://stackoverflow.com/questions/5201708/how-to-return-a-2d-array-from-a-function-in-c

/**
 * It creates a 2D array of floats
 *
 * @param n the number of rows and columns in the matrix
 *
 * @return A pointer to a pointer to a float.
 */
float **createMatx(int n)
{
    float *values = calloc(n * n, sizeof(float));
    float **rows = malloc(n * sizeof(float *));
    for (int i = 0; i < n; ++i)
    {
        rows[i] = values + i * n;
    }
    return rows;
}

/**
 * It frees the memory allocated for the matrix.
 *
 * @param matx The matrix to be destroyed.
 */
void destroyMatx(float **matx)
{
    free(*matx);
    free(matx);
}

void getMinMax(int n)
{
    // Convert int to float
    float var = (float)n / 100 * 100;

    float min = 0, max = 10;

    if (var > 1)
        min = floor((n - 1) / 10) * 10;
    if (var > 0)
        max = ceilf(n / 10.0) * 10;

    // printf("%f : %f\n", min, max);
    printf("%i : %i", (int)min, (int)max);
}

/**
 * It prints a matrix of size n x n
 *
 * @param matx The matrix to be printed
 * @param n the number of rows and columns in the matrix
 */
void printMatx(float **matx, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%f ", matx[i][j]);
        }
        printf("\n");
    }
}

/**
 * This function populates the matrix with random numbers.
 *
 * @param matx the matrix to be populated
 * @param n the size of the matrix
 */
void populateMatx(float **matx, int n)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if ((i % 10 == 0) && (j % 10 == 0))
                matx[i][j] = (rand() % (1000));
}

// void terrain_inter(float** M, int n)
// {
//     for (int i = 0; i < n; i++)
//     {

//     }

//     print()

// }

int main()
{
    int n = 0;
    printf("Enter n divisible by 10: ");
    int check = scanf("%d", &n);

    while (!check || n <= 0 || n%10!=0)
    {
        printf("Wrong Input! Try again: ");
        check = scanf("%d", &n);
    }

    // +1 to include the actual 10th coordinate
    n++;

    // Reinitializes the randomizer for C
    srand(time(NULL));

    float **matx = createMatx(n);
    populateMatx(matx, n);
    // printMatx(matx, n);
    destroyMatx(matx);

    // getMinMax(n);


    return 0;
}