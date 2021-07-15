'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,
.
Both players have to make substrings using the letters of the string

.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string

.

For Example:
String
= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. '''

'''s=input()
scoreStuart=0
scoreKevin=0

def minion_game(string):
	Vocales=['A','E','I','O','U']
	scoreStuart=0
	scoreKevin=0
	#scoreStuart=string.count('A')+string.count('E')+string.count('I')+string.count('O')+string.count('U')
	#scoreKevin=len(string)-scoreStuart
	#lista=[chr(65+i) for i in range(26)]
	for i in range(len(string)):
		for j in range(i+1,len(string)+1):
			aux=string[i:j]
			#if string[i:j]==string[i:j+1]
			if aux[0:1] in Vocales and aux[0:1]!='':
				scoreKevin+=1
			
			elif aux[0:1]!='':
				scoreStuart+=1

				
	if scoreKevin>scoreStuart and scoreKevin-scoreStuart!=1:
		print(f'Kevin {scoreKevin}')
		
	elif scoreStuart>scoreKevin and scoreStuart-scoreKevin!=1:
		print(f'Stuart {scoreStuart}')
		
	else:
		print('Draw')

minion_game(s)'''

S=input()
s=0
k=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
        k+=len(S)-i
    else:
        s+=len(S)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str(s))


	

