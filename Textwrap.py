import textwrap

def wrap(string, max_width):
    lista=textwrap.wrap(string,max_width)
    texto=''
    for i in lista:
    	texto+=i+'\n'
    return texto

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
