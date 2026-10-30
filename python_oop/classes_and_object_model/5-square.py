#!/usr/bin/env python3
"""Define una clase Square que puede imprimir un cuadrado"""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado"""
        self.size = size

    @property
    def size(self):
        """Devuelve la dimension del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza la dimension del cuadrado"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el area del cuadrado"""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado utilizando el caracter #"""
        if self.__size == 0:
            print()
            return
        for row in range(self.__size):
            print("#" * self.__size)
