def decorator(func):
   def wrapper(*args):
      print("Wrapper function executed")
      return func(*args)
   return wrapper


class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"
   def __call__(self,func):
      def wrapper(*args):
         print(self)
         print("Class Wrapper executed")
         return func(*args)
      return wrapper

@A(3,4)
@decorator
def func(*args):
  for i in args:
     print(i)

@decorator
@A(5,6)
def func1(*args):
   for i in args:
      print(i)

if __name__=="__main__":
   func(1,2,3,4)
   func1(5,6,7,8,9)

