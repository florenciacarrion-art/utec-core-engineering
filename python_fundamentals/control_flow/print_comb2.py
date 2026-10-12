#!/usr/bin/env python3

for value in range(0, 100):
    if value < 99:
        print("{:02d}".format(value), end=", ")
    else:
        print("{:02d}".format(value))
