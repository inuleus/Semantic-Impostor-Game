import random
import os

def clearScreen():
    # clears the screen to allow secrecy within the game
    # checks the os to clear accordingly ensuring portability of the game across different op
    os.system('cls' if os.name == 'nt' else 'clear')

def game(players, words):
    # core game logic
    # selects impostor and word to be played
    impostor = players[random.randrange(len(players))]
    target = random.randrange(len(words))
    word,clue = words[target]

    # assigns roles to players
    for player in players:
        input(f"{player}, premi INVIO per vedere la tua parola...\n")
        if player == impostor:
            print(f"\nSEI L'IMPOSTORE\n\nINDIZIO: {clue}\n")
        else:
            print(f"\nLA PAROLA è: {word}\n")
        
        # users control output flow (allowing secrecy needed for the game)

        input("\nPremi INVIO e passa il dispositivo al prossimo giocatore...")
        clearScreen()

    # user controlled impostor reveal
    input("Premi INVIO per rivelare l'impostore...\n")
    print(f"\nL'IMPOSTORE ERA {impostor}\n")

def newGame():
    # allows a new match to happen
    response = input("\nVOLETE CONTINUARE A GIOCARE? (S/N) ").upper()
    if response == 'S':
        return True
    else:
        return False


def setPlayers():
    # dynamic players set up
    n_player = int(input("QUANTI GIOCATORI CI SONO? "))
    players = []

    for n in range(n_player):
        players.append(input(f'NOME GIOCATORE {n+1}: ').strip().upper())
    
    return players

def getWords():
    # parsing of the words and relative semantic related clues
    words = []
    try:
        with open("corpus.txt", 'r', encoding='utf-8') as inF:
            for line in inF:
                data = line.split()
                if len(data) >= 2:
                    words.append((data[0], data[1]))
    except FileNotFoundError:
        print("File 'corpus.txt' non trovato. Caricamento parole di default.")
        words = [("Python", "Linguaggio"), ("Cervello", "Cognizione")]
    return words


if __name__ == "__main__":
    players = setPlayers()
    words = getWords()

    if not words:
        print("Errore: Il corpus è vuoto. Impossibile giocare.")
    else:
        go_on = True
       
        # loop that allows multiple matches
        
        while go_on:
            clearScreen()
            game(players, words)
            go_on = newGame()