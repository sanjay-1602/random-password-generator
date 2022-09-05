from dicewareMap import dicewareMap as dwMap
from typing import List, Any
from secrets import randbelow
from string import punctuation


# <editor-fold desc="[Prettier Printing Functions]">
def success(msg: str, val: Any = None) -> None:
    if val is None:
        print("[+]: {}".format(msg))
        return
    print("[+]: {}{}".format(msg, val))
    return


def error(msg: str, val: Any = None) -> None:
    if val is None:
        print("[-]: {}".format(msg))
        return
    print("[-]: {}{}".format(msg, val))
    return


def info(msg: str, val: Any = None) -> None:
    if val is None:
        print("[*]: {}".format(msg))
        return
    print("[*]: {}{}".format(msg, val))
    return
# </editor-fold>


# <editor-fold desc="[Internal Implementation Functions]">
def getRandomNumber(exclusive_max: int, singular: bool) -> int:
    if singular:
        rv_singular = randbelow(exclusive_max)
        return rv_singular
    rv_s: str = ""
    rNums: List[int] = []
    for i in range(0, 5):
        num: int = randbelow(exclusive_max)
        if num == 0:
            num = 1
        rNums.append(num)
    for i in rNums:
        rv_s += str(i)
    return int(rv_s)


def getUserInput(msg: str, upper_bound: int) -> int:
    rvUI: int
    try:
        info(msg)
        rvUI = int(input())
        if rvUI > upper_bound or rvUI < 0:
            error("Number too big or negative, please retry...")
            return getUserInput(msg, upper_bound)
        return rvUI
    except ValueError:
        error("Input not recognized, please retry...")
        return getUserInput(msg, upper_bound)


def getWordFromDicewareMap(key: int) -> str:
    return dwMap.get(key)


def removeSpaces(password: str) -> str:
    return password.replace(" ", "")


def substituteSpaceWithSpecialChars(password_orig: str) -> str:
    spChars: List[str] = list(punctuation)
    pwList: List[str] = list(password_orig)
    for i in range(0, len(pwList)):
        if pwList[i] == " ":
            idx = getRandomNumber(32, True)
            pwList[i] = spChars[idx]
    password: str = "".join(pwList)
    return password


def substituteWithRandomNumbers(password_orig: str) -> str:
    pwList: List[str] = list(password_orig)
    replacableChars: List[str] = ["a", "b", "e", "z", "s", "t", "i", "g", "o"]
    for i in range(0, len(pwList)):
        if pwList[i] in replacableChars:
            num = getRandomNumber(10, True)
            pwList[i] = str(num)
    password: str = "".join(pwList)
    return password
# </editor-fold>

'''
if __name__ == '__main__':
    dwPassword: str = ""
    wIndices: List[int] = []

    nWords = getUserInput("How many words would you like to use? :", 7776)

    for i in range(0, nWords):
        rNumber: int = getRandomNumber(7, False)
        wIndices.append(rNumber)

    for i in range(0, nWords):
        word: str = getWordFromDicewareMap(wIndices[i])
        dwPassword += word
        if i != nWords-1:
            dwPassword += " "

    shouldUseSpecialChars: int = getUserInput("Would you like to replace spaces with special characters? (1)yes or (0)no :", 1)
    if shouldUseSpecialChars == 1:
        dwPassword = substituteSpaceWithSpecialChars(dwPassword)
    else:
        dwPassword = removeSpaces(dwPassword)

    shouldUseNumbers: int = getUserInput("Would you like to replace common characters with random numbers?: (1)yes or (0)no :", 1)
    if shouldUseNumbers == 1:
        dwPassword = substituteWithRandomNumbers(dwPassword)

    success("Your password in accordance to diceware is as follows\n", dwPassword)
    info("Password length: ", len(dwPassword))
'''
