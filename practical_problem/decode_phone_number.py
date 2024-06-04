letterToDigit = {
  'A':'2', 'B':'2', 'C':'2',
  'D':'3', 'E':'3', 'F':'3',
  'G':'4', 'H':'4', 'I':'4',
  'J':'5', 'K':'5', 'L':'5',
  'M':'6', 'N':'6', 'O':'6',
  'P':'7', 'Q':'7', 'R':'7', 'S':'7',
  'T':'8', 'U':'8', 'V':'8',
  'W':'9', 'X':'9', 'Y':'9', 'Z':'9',
  }

digitToLetters = {
  '2':['A','B','C'],
  '3':['D','E','F'],
  '4':['G','H','I'],
  '5':['J','K','L'],
  '6':['M','N','O'],
  '7':['P','Q','R','S'],
  '8':['T','U','V'],
  '9':['W','X','Y','Z']
}

def decodePhoneNumber(text):
    res = ""
    for char in text.upper():
        if char in letterToDigit:
            res += letterToDigit[char]
        else:
            res += char

    for index, char in enumerate(text):
        print(index, char)

    return res



    
print(decodePhoneNumber("1-800-U-B-SMART") == "1-800-8-2-76278")
print(decodePhoneNumber("1.800.I.C.BUTTS") == "1.800.4.2.28887")
print(decodePhoneNumber("1-888-GET-RICH") == "1-888-438-7424")
print(decodePhoneNumber("555-U-HUNGRY!") == "555-8-486479!")
print(decodePhoneNumber("ORANGES") == "6726437")
print(decodePhoneNumber("C O C O N U T") == "2 6 2 6 6 8 8")
print(decodePhoneNumber("B_A_N_A_N_A_S") == "2_2_6_2_6_2_7")
print(decodePhoneNumber("I 1 I 1 I 1 I") == "4 1 4 1 4 1 4")
print(decodePhoneNumber("1111 AaBb CcDd EeFf 1111") == "1111 2222 2233 3333 1111")
print(decodePhoneNumber("777 EcsTaSy 777") == "777 3278279 777")
print(decodePhoneNumber("") == "")