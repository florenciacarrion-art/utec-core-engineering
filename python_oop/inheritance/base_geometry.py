#!/usr/bin/env python3
"""Define la clase base para figuras geometricas"""


class BaseGeometry:
    """Representa la geometria basica"""

    def area(self):
        """El calculo del area no esta implementado"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor represente un entero positivo valido"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
