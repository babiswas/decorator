class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b

   def __str__(self):
      return f"{self.a} and {self.b}"

   def __call__(self,func):
      def wrapper(*args):
         print("Wrapper function executed")
         print(self)
         return func(*args)
      return wrapper

@A(3,4)
def func2(*args):
   print("Inside the function")
   for i in args:
      print(i)

if __name__=="__main__":
   func2(1,2,3,4)

