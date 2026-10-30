#!/usr/bin/env python3
"""Define una clase Square que puede imprimir un cuadrado"""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Devuelve la posicion del cuadrado"""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y actualiza la posicion del cuadrado"""
        if (type(value) is not tuple or len(value) != 2
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0 or value[1] <0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Devuelve el area del cuadrado"""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado utilizando el caracter #"""
        print(self)

    def __str__(self):
        """Devuelve el cuadrado como una cadena de texto"""
        if self.__size == 0:
            return ""

        space = " " *self.__position[0]
        rows = [""] * self.__position[1]

        for row in range(self.__size):
            rows.append(space + "#" * self.__size)

        return "\n".join(rows)
