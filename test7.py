class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __gt__(self,other):
     if isinstance(other,A):
        if other.a>self.a:
           return True
        else:
           return False
     else:
        raise Exception


  def __str__(self):
     return f"{self.a} and {self.b}"

  def __lt__(self,other):
      if isinstance(other,A):
         if self.a>other.a:
            return True
         elif self.a<other.a:
            return False
      else:
         raise Exception

  def __enter__(self):
      print("I am in enter block")
      print(self.__dict__)
      return self

  def __exit__(self,exc_type,exc_val,exc_tb):
      print("Exit method called")

  def __sub__(self,other):
      if isinstance(other,A):
         return f"{other.a-self.b} is the value"
      else:
         raise Exception

  def __add__(self,other):
      if isinstance(other,A):
         return f"{self.a+other.a} is the value"
      else:
         raise Exception

  def display(self):
     print(f"{self.a} and {self.b}")

if __name__=="__main__":
   with A(3,4) as a:
      a.display()
      b=A(10,4)
      print(a+b)
      print(a-b)
      print(a<b)
      print(a>b)
      print(a)
      print(b)

