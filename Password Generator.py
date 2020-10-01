from random import *
import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
num = "0123456789"
char = "!@#$%^&* -+="


def intro():
    print("Password Generator by Kichi Choi")
    global length
    length = int(input("Hello. How long do you need the password to be?: "))
    randomChar()


def randomChar():
    randUpper = randint(1, length)
    randLower = randint(1, length)
    randNum = randint(1, length)
    randChar = randint(1, length)

    if (randUpper+randLower+randNum+randChar) != length:
        randomChar()
    else:
        return passGen(randUpper, randLower, randNum, randChar)



def passGen(randUpper, randLower, randNum, randChar):
    password = ""
    for i in range(randUpper):
        password += choice(upper)
    for j in range(randLower):
        password += choice(lower)
    for k in range(randNum):
        password += choice(num)
    for l in range(randChar):
        password += choice(char)

    pass_word = list(password)
    #print(pass_word)

    # random.sample(pass_word, len(pass_word))
    # shuffled = sorted(pass_word, key=lambda k:random.random)
    # print(shuffled)

    random.shuffle(pass_word)
    #print(pass_word)
    #shuff = random.shuffle(pass_word, len(pass_word))
    # print(shuff)
    newPass = "".join(pass_word)
    print(newPass)
    return newPass


intro()
