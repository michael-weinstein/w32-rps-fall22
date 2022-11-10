import random
import typing

def getPlayerThrow(winTable:typing.Dict[str, str]) -> str:
    playerThrow = input("rock, paper, or scissors? ")
    return playerThrow

def getComputerThrow(winTable:typing.Dict[str, str]) -> str:
    possibleThrows = list(winTable.keys())
    return random.choice(possibleThrows)

def determineOutcome(winTable:typing.Dict[str, str], computerThrow:str, playerThrow:str) -> None:
    if playerThrow == computerThrow:
        return print('Tie')
    elif computerThrow == winTable[playerThrow][0]:
        return print('You lost :(')
    elif playerThrow == winTable[computerThrow][0]:
        return print('You won!')

def playARound(winTable:typing.Dict[str, str]) -> None:
    playerThrow = getPlayerThrow(winTable)
    print("You selected", playerThrow)
    computerThrow = getComputerThrow(winTable)
    print("Computer selected", computerThrow)
    determineOutcome(winTable, computerThrow, playerThrow)