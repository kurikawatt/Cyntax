"""
argsParser, part of the Cyntax program
Version : NONE

Created on November 2nd of 2022
Last update : 
Licence : MIT
Author : François "Kurikawa", kurikawatt on GitHub
"""


def argsSort(args:list) -> None:
    """
    Sort the provided args list

    In Cyntax, I need an input file, and it must be the first arg
    """
    for i, value in enumerate(args):
        #if value looks like ****.c 
        if value[-2:] == ".c":
            #permutation between the first and the i-th element
            args[0], args[i] = args[i], args[0]
            break

def getParameters(args:list) -> dict:
    """
    Return a dictionnary of valid parameters for Cyntax
    """
    #First, sort args
    argsSort(args)
    #By default, a parameter is disabled
    param = {
        "file": args[0],
        "semicolon": False,
        "correct": False,
        "export": False,
        "export_name": "out.c",
    }
    for i, arg in enumerate(args):
        single_arg = (arg[0] == "-" and arg[1] != "-") #To detect arg like "-xx" and not like "--xxxxxxx"
        if arg == "--semicolon" or (single_arg and "s" in arg):
            param["semicolon"] = True
        if arg == "--correct" or (single_arg and "c" in arg):
            param["correct"] = True
        if arg == "--export" or (single_arg and "e" in arg):
            param["export"] = True
    return param

    

#Tests
if __name__ == "__main__":
    testA = ["file.c", "-cs"]
    testB = ["-cs", "file.c", "--export", "out.c"]
    testC = ["-c", "-s", "file.c", "--export", "out.c"]
    tests = [testA, testB, testC]
    for test in tests:
        argsSort(test)
        print(test)
        print(getParameters(test))