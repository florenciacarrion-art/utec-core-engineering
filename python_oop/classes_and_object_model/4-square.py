#!/usr/bin/env python3
"""Define una clase Square con acceso controlado al tamaño"""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño determinado"""
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y actualiza el tama�o del cuadrado"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
           raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el area del cuadrado"""
        return self.__size * self.__size
