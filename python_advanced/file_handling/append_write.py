#!/usr/bin/env python3
"""Añadir contenido"""


def append_write(filename="", text=""):
    """Añadir una cadena de texto al final de un archivo."""
    with open(filename, "a", encoding="utf-8") as file:
        added = file.write(text)

    print(added)
