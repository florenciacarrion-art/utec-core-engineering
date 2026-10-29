#!/usr/bin/env python3
"""Define una clase Square con validacion de tamaño"""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado y valida su tamaño"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
