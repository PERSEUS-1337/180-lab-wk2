# CMSC 180 - Week 2 - Lab 01 Part 2
## Author
Author: Aron Resty Ramillano | 2020-01721
Section: T3L

## App Description
This is a revision of my first python file that uses Area Weighted Interpolation to calculate the missing values in a matrix, given that there are 4 given values to be used as anchor and basis for the calculation.

## Features
 1. It can calculate matrices that is divisible by 10 with high performance using the C language
 2. This revision has a benchmark that can test the program's performance with 3 passes on calculating matrices ranging from 100 to 20000

## Files included:
 - lab01-2.c
 - n_vs_runtime_complexity.xlsl
 - Ramillano_labreport_exer2.pdf
 - README.md
  
## How to setup
 - Must have GCC
 - Run this command:
	 - `gcc -o a lab01-2.c -lm; ./a`
	 - The `-lm` enables the `<math.h>` library for use of the `ceil` and `floor` functions

# Resources
- https://www.geeksforgeeks.org/multidimensional-arrays-c-cpp/
- https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/
- https://stackoverflow.com/questions/5201708/how-to-return-a-2d-array-from-a-function-in-c