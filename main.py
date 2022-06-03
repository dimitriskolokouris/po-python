import random
wordlist =
["programmeren","galgje","quiz","woordenlijst","chocoladereep"]

def get_word(wordlist):
 word = random.choice(wordlist) 
 return word.upper()


def question():
  x = 0
   while x < 2:
     