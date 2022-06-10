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

#Spel Begint
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
        print(guess, "letter is niet in het woord: ")
        tries -= 1
        guessed_letters.append(guess)

#Galgje mannetje verschillende staten
def display_hangman(tries):
  stages = []