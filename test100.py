def decorator(func):
   def wrapper(*args,**kwargs):
       print("Wrapper function executed")
       return func(*args,**kwargs)
   return wrapper

@decorator
def func(*args):
   for i in args:
      print(i)

if __name__=="__main__":
   func(1,2,3,4,5)
