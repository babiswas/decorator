def decorator(cls):
   def wrapper(*args):
      print("Wrapper function executed")
      def func(self,a,b):
          return a+b
      setattr(cls,'add',func)
      return cls(*args)
   return wrapper


@decorator
class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
  a=A(5,6)
  print(a)
  print(a.add(3,4))