import random
import typing

def playerThrowInvalid(playerThrow: int) -> bool:
    """
    Checks that the player input is within the allowed values
    :param playerThrow:
    :return:
    """
    if playerThrow not in set([0, 1, 2]):
        return True
    return False

def getPlayerThrow(winTable:typing.Dict[str, str]) -> str:
    playerThrow = input("rock (0), paper (1), or scissors (2)? ")
    if playerThrowInvalid(playerThrow):
        print('Input in valid. Please input 0, 1, or 2')
        return getPlayerThrow(winTable)
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