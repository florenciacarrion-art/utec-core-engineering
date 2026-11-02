#!/usr/bin/env python3
"""Define un rectangulo con area"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectangulo"""

    def __init__(self, width, height):
        """Inicializa un rectangulo validando sus dimensiones"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el area del rectangulo"""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve una representacion legible del rectangulo"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
