#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = " ".join("{:d}".format(value) for value in row)
        print(line)
