#filter odd even
#define a function
#input list = [1,2,3,4,5,6,7]
#ouput [[1,3,5,7],[2,4,6]]

def odd_even(list):
	list_odd=[]
	list_even=[]
	listEnd=[]
	for i in list:
		if i%2==0:
			list_even.append(i)
		else:
			list_odd.append(i)
	listEnd.append(list_odd)
	listEnd.append(list_even)
	return listEnd
	
lista=[1,2,3,4,5,6,7]
print(odd_even(lista))
	
