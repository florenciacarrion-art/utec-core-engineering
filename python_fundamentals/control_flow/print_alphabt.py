#!/usr/bin/env python3

for letra in range(ord('a'), ord('z') + 1):
    if chr(letra) != "e" and chr(letra) != "q":
        print("{}".format(chr(letra)), end="")
