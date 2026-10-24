#!/usr/bin/env python3
"""Módulo para leer archivos de texto."""


def read_file(filename=""):
    """Lee el contenido de un archivo y lo imprime en pantalla."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
