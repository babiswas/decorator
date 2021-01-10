class Test:
   def __init__(self):
       self.test_factory=dict()
   def decorator(self,datatype):
       def wrapper(func):
          if datatype=='A':
             self.test_factory[datatype]=func
          elif datatype=='B':
             self.test_factory[datatype]=func
          else:
             self.test_factory[datatype]=func
       return wrapper
   def run(self,*args,**kwargs):
       for key in self.test_factory.keys():
           self.test_factory[key](*args,**kwargs)

test=Test()

@test.decorator('A')
def func1(*args):
   print(args)

@test.decorator('B')
def func2(*args):
   print(args)

@test.decorator('C')
def func3(*args):
    print(args)

if __name__=="__main__":
   test.run("hello","bello")


