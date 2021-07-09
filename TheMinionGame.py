s=input()
score=0
def minion_game(string):
	score=0
	vocales=['A','E','I','O','U']
	lista=[]
	for i in string:
		if i not in vocales and i not in lista:
			score+=string.count(i)
			lista.append(i)
	for i in range(len(string)+1):
		for j in range(2,len(string)):
			if lista[i:j] not in lista and string[i:j]!="" and len(string[i:j])>1\
				 and string[i:j][0] not in vocales:			
				score+=string.count(string[i:j])
				lista.append(string[i:j])
				print(string[i:j])
	print(lista)
	return score		

print(minion_game(s))


