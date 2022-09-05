import alphanum as al
import dWMain as dice
import dicewareMap
import pronounce as pro
import random
import string
from typing import List, Any
from secrets import randbelow
from string import punctuation
import sys
#from Alphanum import *
print("--------Random Password Generator--------------")
print("1.Alphanumeric Generator\n2.Diceware Passphrase Generator\n3.Pronounce Generator")
print("-----------------------------------------------")
choice=int(input("Enter your choice:"))
if(choice==1):
  lc=int(input("Enter letter count:"))
  dc=int(input("Enter Digit count:"))
  al.get_string(lc, dc)
elif(choice==2):
  dwPassword: str = ""
  wIndices: List[int] = []
  nWords = dice.getUserInput("How many words would you like to use? :", 7776)

  for i in range(0, nWords):
        rNumber: int = dice.getRandomNumber(7, False)
        wIndices.append(rNumber)

  for i in range(0, nWords):
        word: str = dice.getWordFromDicewareMap(wIndices[i])
        dwPassword += word
        if i != nWords-1:
            dwPassword += " "
  shouldUseSpecialChars: int = dice.getUserInput("Would you like to replace spaces with special characters? (1)yes or (0)no :", 1)
  if shouldUseSpecialChars == 1:
        dwPassword = dice.substituteSpaceWithSpecialChars(dwPassword)
  else:
        dwPassword = dice.removeSpaces(dwPassword)

  shouldUseNumbers: int = dice.getUserInput("Would you like to replace common characters with random numbers?: (1)yes or (0)no :", 1)
  if shouldUseNumbers == 1:
        dwPassword = dice.substituteWithRandomNumbers(dwPassword)
  dice.success("Your password in accordance to diceware is as follows\n", dwPassword)
  dice.info("Password length: ", len(dwPassword))      
elif(choice==3):
  prng = random.SystemRandom()
  templates = pro.make_templates(4, 4)
  for n in range(1,21):
      password = pro.make_password(prng, templates)
      print(f"{n}. {password}")
  print("Press enter.")
  sys.stdin.readline()
  sys.exit(0)
else:
  print("Wrong Choice")
