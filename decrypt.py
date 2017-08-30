characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',',';',':','[',']','{','}','(',')','+','-','/','*','>','<','=','"',' ']


def decToTert(dec):
    result = ""

    for n in range(3,-1,-1):
        if dec >= 2*(3**n):
            dec -= 2*(3**n)
            result += "2"
        elif dec >= 3**n:
            dec -= 3**n
            result += "1"
        else:
            result += "0"
    return result

def tertToDec(tert):
    result = 0

    for n in range(0,4):
        result += int(tert[n])*3**(3-n)
    return result

message = input("Message: ")

tert = []
plain = []
for letter in message:
    tert.append(decToTert(characters.index(letter)))
    plain.append("")

count = 0
for word in tert:
    for letter in word:
        plain[count] += letter
        count += 1
        if count >= len(plain):
            count = 0

final = ""
for word in plain:
    final += characters[tertToDec(word)]

print(final)
