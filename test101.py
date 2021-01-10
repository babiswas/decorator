def decorator1(func):
   def wrapper(*args,**kwargs):
       print("Wrapper 1 of decorator 1 executed")
       return func(*args,**kwargs)
   return wrapper


def decorator2(func):
   def wrapper(*args,**kwargs):
       print("Wrapper 2 of decorator 2 executed")
       return func(*args,**kwargs)
   return wrapper


@decorator2
@decorator1
def func(*args):
   for i in args:
       print(i)

if __name__=="__main__":
   func(1,2,3,4)