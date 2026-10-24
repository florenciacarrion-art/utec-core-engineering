#!/usr/bin/env python3
"""Módulo para escribir texto en un archivo."""


def write_file(filename="", text=""):
    """Escribe texto en un archivo y devuelve la cantidad de caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
