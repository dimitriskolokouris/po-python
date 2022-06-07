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
  word_completion = "_" * len*(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  
     
