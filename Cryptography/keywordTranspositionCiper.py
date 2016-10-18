import string    
import math


n= int(input())

msg = ""
for i in range(0,n):
	keyWord1 = input()
	cipherText = input()

	keyWord = ""
	for i in keyWord1:
		if i not in keyWord:
			keyWord+=i

	list1 = []
	for i in range(ord('A'),ord('Z')+1):
		if(chr(i) not in keyWord):
			list1.append(chr(i))

	chunks = [list1[i:i+len(keyWord)] for i in range(0,len(list1),len(keyWord))]
	chunks.insert(0,list(keyWord))

	chunks2 = [None] * len(chunks) 
	for i in range(0,len(chunks)):
		chunks2[i] = [" "]*len(keyWord)
		for j in range(0,len(chunks[i])):
			chunks2[i][j] = chunks[i][j]

	list2 = list(zip(*[element for element in chunks2]))
	
	list2.sort()
	list2 = [j for i in list2 for j in i if (j!= " ")]

	dict1 = {}
	for i in range(ord('A'),ord('Z')+1):
		dict1[list2[i-ord('A')]] = chr(i)
		
	for i in cipherText : 
		if (i != " "):
			msg+=dict1[i]
		else:
			msg+=" "
	msg+="\n"
			
print (msg[:-1])