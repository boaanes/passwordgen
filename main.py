from random import randint

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pws = []

def pwgen(length):
    pw = ""

    i = 0
    while(i < length):
        arrindex = randint(0, len(chars) - 1)
        charCase = randint(0, 1)

        if(charCase == 0):
            pw += str(chars[arrindex])
        elif(charCase == 1):
            pw += str(chars[arrindex].upper())
        i += 1

    pws.append(pw)

def gen(num, length):
    string = ""

    for i in range(num):
        pwgen(length)

    for i in range(len(pws)):
        string += "Password " + str(i + 1) + ": " + pws[i] + "\n"

    return string

def writefile(num, length):
    file = open('passwords.txt', "w")
    file.write(gen(num, length) + "\n")
    file.close()

writefile(10, 15)