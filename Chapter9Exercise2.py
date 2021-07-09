#num to string
#define a function

#example
#input -----> [True, False,[1,2,3],1,1.0, 3]
#output -----> ['1','1.0','3']

def NumToString(lista):
	nuevaLista=[str(i) for i in lista if type(i)==type(1) or type(i)==type(2.3)]
	return nuevaLista

lista=[True, False,[1,2,3],1,1.0, 3]
print(NumToString(lista))


