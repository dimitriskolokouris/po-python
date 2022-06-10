#Woordenlijst
import random
word_list = ["informatica","informatiekunde","spelletje","aardigheidje","scholier","fotografie","waardebepaling","specialiteit","verzekering","universiteit","heesterperk"]

def get_word(word_list):
  word = random.choice(word_list)
  return word.upper()

#Introductiescherm
def question():
  i = 0 
  while i < 2:
    answer = input("Welkom! Wil je galgje spelen? (Ja of Nee)")
    if any(answer.lower() == f for f in ["Ja", 'J', 'ok', 'Y']):
        print("Kom op dan!")
        break

    else:
     i+=1
     if i < 2:
       print("Weet je het zeker?")
     else:
       print("Je moet!!!")

#Spel Begin-Tussendoor-Einde
question()
def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Je mag nu een letter invullen!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess= input("Raad een letter of het woord").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("Je hebt deze letter al geprobeerd: ", guess, "!")
      elif guess not in word:
        print(guess, "letter is niet in het woord :(")
        tries -= 1
        guessed_letters.append(guess)
      else:
          print("Goed zo,", guess , "is in het woord!")
          guessed_letters.append(guess)
          word_as_list = list(word_completion)
          indices = [i for i, letter in enumerate(word) if letter == guess]
          for index in indices:
            word_as_list[index] = guess
          word_completion = "".join(word_as_list)
          if "_" not in word_completion:
            guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words: 
        print("Je hebt dit al geprobeerd:", guess, "!")
      elif guess != word:
        print(guess, "is niet in het woord :(")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        word_completion = word
    else:
      print("ongeldige input")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
    if guessed:
      print("Goed zo, je hebt het woord geraden!")
    else:
      print("HELAAS! JE HEBT GEEN GOKKEN MEER. Het woord was" + word + ".Misschien heb je volgende keer meer geluk!")
      
#Galgje mannetje verschillende staten
def display_hangman(tries):
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
  return stages[tries]
#Vraag of je nog een keer wil spelen
def main():
  word = get_word(word_list)
  play(word)
  while input("Wil je nog een keer galgje spelen? (Ja/Nee) ").upper() == "J":
    word = get_word(word_list)
    play(word)

if __name__ == "__main__":
  main()