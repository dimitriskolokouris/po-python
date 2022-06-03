import random
word_list = ["informatica","galgje","python","programmeren","maartenscollege"]

def getword(word_list):
  word = random.choice(word_list)
  return word.upper()


def question():
  x = 0
  while x < 2:
    answer = input("Hallo speler, wil je een potje Galgje spelen? (ja of nee)")
    if any(answer.lower() == f for f in ["ja"]):
      print("Veel speelplezier!")
      break
    
    else:
      x += 1
      if x < 2:
        print("Weet je het zeker?")


question()
      