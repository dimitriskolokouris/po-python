# Woordenlijst
import random
woordenlijst = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

def get_woord(woordenlijst):
    woord = random.choice(woordenlijst)
    return woord.upper()
# Introductiescherm + tekst
def question():
    i = 0
    while i < 2:
        antwoord = input("Welkom! Wil je galgje spelen? (Ja of Nee)")
        if any(antwoord.lower() == f for f in ["Ja", 'J', 'ja', 'Y']):
            print("Kom op dan!")
            break
        
        else:
            i += 1
            if i < 2:
                print('Weet je het zeker?')
            else:
                print("Je moet!")

# Spel Begin-Tussendoor-Eind + tekst
question()
def play(woord):
    woordaanvulling = "_" * len(woord)
    geraden = False
    geraden_letters = []
    geraden_woorden = []
    kansen = 6
    print("Je mag nu een letter invullen!")
    print(galgjemannetje(kansen))
    print(woordaanvulling)
    print("\n")
    while not geraden and kansen > 0:
        raadsel = input("Raad een letter of woord: ").upper()
        if len(raadsel) == 1 and raadsel.isalpha():
            if raadsel in geraden_letters:
                print("Je hebt deze letter al geprobeerd: ", raadsel, "!")
            elif raadsel not in woord:
                print(raadsel, "is niet in het woord :(")
                kansen -= 1
                geraden_letters.append(raadsel)
            else:
                print("Goed zo,", raadsel, "is in het woord!")
                geraden_letters.append(raadsel)
                woord_as_list = list(woordaanvulling)
                indices = [i for i, letter in enumerate(woord) if letter == raadsel]
                for index in indices:
                    woord_as_list[index] = raadsel
                woordaanvulling = "".join(woord_as_list)
                if "_" not in woordaanvulling:
                    geraden = True
        elif len(raadsel) == len(woord) and raadsel.isalpha():
            if raadsel in geraden_woorden:
                print("Je hebt dit al geprobeerd: ", raadsel, "!")
            elif raadsel != woord:
                print(raadsel, " is niet het woord :(")
                kansen -= 1
                geraden_woorden.append(raadsel)
            else:
                geraden = True
                woordaanvulling = woord
        else:
            print("ongeldige input")
        print(galgjemannetje(kansen))
        print(woordaanvulling)
        print("\n")
    if geraden:
        print("Goed zo, je hebt het woord geraden!")
    else:
        print("Het spijt me, maar je hebt geen gokken meer. Het woord was " + woord + ". Misschien heb je volgende keer meer geluk!")

# Galgje mannetje tekeningen
def galgjemannetje(kansen):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[kansen]

# Nog een keer spelen?
def main():
    woord = get_woord(woordenlijst)
    play(woord)
    while input("Wil je nog een keer galgje spelen? (J/N) ").upper() == "J":
        woord = get_woord(woordenlijst)
        play(woord)


if __name__ == "__main__":
    main()