import random
import typing

def getPlayerThrow(winTable:typing.Dict[str, str]) -> str:
    pass

def getComputerThrow(winTable:typing.Dict[str, str]) -> str:
    possibleThrows = list(winTable.keys())
    return random.choice(possibleThrows)

def determineOutcome(winTable:typing.Dict[str, str], computerThrow:str, playerThrow:str) -> str:
    pass

def playARound(winTable:typing.Dict[str, str]) -> typing.Tuple[str,str]:
    pass