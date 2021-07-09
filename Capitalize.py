s=input()
def solve(s):
	l=s.split(" ")
	texto=""
	for i in l:
		if i!="":
			texto+=i.capitalize()+" "
		else:
			texto+=" "
	return texto
print(solve(s))
