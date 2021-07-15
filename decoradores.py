def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function()

@decorator_function
def func1():
        print('esta es la funcion uno')


func1()



