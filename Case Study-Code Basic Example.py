import sys
#Lookup Map Letter to Number 1
charToNumberMap = {' ': -1, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13 , 'N': 14, 'O': 15, 'P': 16,'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26 }
NumberTocharMap = {26: 'A', 25: 'B', 24: 'C', 23: 'D', 22: 'E', 21: 'F', 20: 'G', 19: 'H', 18: 'I', 17: 'J', 16: 'K', 15: 'L', 14: 'M', 13: 'N', 12: 'O', 11: 'P', 10: 'Q', 9: 'R', 8: 'S', 7: 'T', 6: 'U', 5: 'V', 4: 'W' ,3: 'X', 2: 'Y', 1: 'Z' , 0: ' ' }

# get the next Name in Letters
Original_NAME = "ROBERTA EIKELSTEIN"
print (Original_NAME)

# use encrypt function to replace 
text = Original_NAME.replace('A', 'K').replace('R', 'P').replace('E','G').replace('I','T').replace('S','Y').replace('K','L')
print (text)

#Lookup Letter to Number and save
lstinputNumbers = []
for elem in text:
	lstinputNumbers.append(charToNumberMap[elem]+1)
print(lstinputNumbers)
 
#Lookup NewNumber to Letter and save
lstoutputEncrypt2 = []
for elem in lstinputNumbers:
	lstoutputEncrypt2.append(NumberTocharMap[elem])
str1 = ''.join(lstoutputEncrypt2)
print(str1)

# use encrypt3 function to replace 
outputEncryptFinal = str1.replace('O', 'K').replace('E', 'T').replace('S','I')
print (outputEncryptFinal)