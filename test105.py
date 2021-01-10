def decorator1(*args,**kwargs):
    def wrapper(func):
        print("Wrapper function executed")
        return func(*args,**kwargs)
    return wrapper


@decorator1("hello","bello","mello",test1="kello",test2="nello")
def func(*args,**kwargs):
   print(args)
   print(kwargs)


  