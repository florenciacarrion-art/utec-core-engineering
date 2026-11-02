#!/usr/bin/env python3
"""Define la clase Square"""

Rectangle = __import__("1-rectangle").Rectangle


class Square(Rectangle):
    """Representa un cuadrado"""

    def __init__(self, size):
        """Inicializa un cuadrado"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Representacion del cuadrado"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Calcula el área del cuadrado"""
        return self.__size ** 2
