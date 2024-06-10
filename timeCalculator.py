import time 
import functools

# decorator
def log_function_call(func): #outer function
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #inner function 
        func(*args,**kwargs)
        return  print(f'function {func.__name__} called') 
    return wrapper

def time_calc(func): #higher order function 
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #inner function
        start= time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end -start
        print(f'Function {func.__name__} took {duration} seconds to execute')
        return result
    return wrapper 


def secure_function(passw):
    def decorator(func):
        def wrapper(*args, **kwargs):
            systemPassword='123'     
            if systemPassword == passw: 
                result= func(*args, **kwargs)
                return result
            print('!! access denied !!')
        return wrapper
    return decorator
                
                
@time_calc
@log_function_call
def simple_func():
    time.sleep(3)
    print('simple func ran')


simple_func()

password=input('type your password: ')

@secure_function(password)
def top_secret():
    print(' Area 51 is real man, they got aliens down there')

top_secret()






# import time
# import functools


# def logFunctionCall(func):

#     def wrapper (*args,**kwargs):
#         func(*args,**kwargs):
#         return print(f'function {func.__name__} called')
#     return wrapper


# def timeCalc(func):
#     @functools.wraps(func)
#     def warpper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end =time.time()
#         duration=end - start
#         print(f'Function {func.__name__} took {duration} seconds to execute')
#         return result
#     return warpper

# def secureFunction (passw):
#     def decorator (func):
#         def wrapper()
            



# @time_calc
# @logFunctionCall
# def simpleFunc():
#     time.sleep(3)
#     print('simple func ran')

# simpleFunc()
# password='123'

# @secureFunction(password)
# def topSecret():
#     print('Area 51 is real man, they got aliens down there!')