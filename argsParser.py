"""
argsParser, part of the Cyntax program
Version : NONE

Created on November 2nd of 2022
Last update : 
Licence : MIT
Author : François "Kurikawa", kurikawatt on GitHub
"""


def argsSort(args:list) -> list:
    """
    Sort the provided args list.

    In Cyntax, I need an input file, and it must be the first arg.
    """
    for i, value in enumerate(args):
        if value[-2:] == ".c":
            args[0], args[i] = args[i], args[0]
            break
    return args

