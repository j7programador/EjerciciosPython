names=['jorge','toti']

def func(names,**kwargs):
	if kwargs.get('reverse_str')==True:
	
		lista=[]
		for i in names:
			lista.append(i[::-1].capitalize())
		return lista

print(func(names,reverse_str=True))



