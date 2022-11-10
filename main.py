import rpsSupport

if __name__ == "__main__":
    while True:
        winTable = rpsSupport.standardWins
        rpsSupport.game.playARound(winTable)
        
        inp = input("Want to play again? y/n ")
        if inp == "y":
            continue
        else:
            break
