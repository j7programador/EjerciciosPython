#This is challenge
# define a function take any no of list containing number

l1,l2,l3=[1,2,3], [4,5,6],[7,8,9]
#return average
#(1+4+7)/3,(2,5,8)/3,(3,6,9)/3

# try to make this anonymous function in one line using lambda

#def func(*args):
#	promedios=tuple(map(lambda x: sum(x)/len(x),args))
#	return promedios

#print(func(l1,l2,l3))

#other method

def average_finder(*args):
	average=[]
	for pair in zip(*args):
		average.append(sum(pair)/len(pair))
	return average

print(average_finder(l1,l2,l3))


promedios= lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]

print(promedios(l1,l2,l3))





		
