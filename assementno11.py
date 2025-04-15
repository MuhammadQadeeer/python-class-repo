# class student():
#     name=input("enter a name")
#     age=input("enter a no")
# std=student()
# print(std.name)

# class student:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def printproporty(self):
#         print(self.name,self.age)
# std=student()
# std.printproporty() 
# class teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def info(self):
#        print(f"{self.name},{self.subject}is teacher info")
# std1=teacher(input("enter a number"), input("enter a subject")) 
# std1.info() 

class car:
    def __init__(self,model,color,model_name):
        self.model_name=model_name
        self.model=model
        self.color=color
    def info(self):
        print(f"car model_name={self.model_name},color={self.color},model={self.model}")
a=car(2024,"black","civic")
a.info()

# import logging
# def log_function(func):
#     def decoraded(*args,**kwargs):
#         logging.info(f"calling{func.__name__}with arg={args},kwarg{kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"{func.__name__}return{result}")
#         return result
#     return decoraded
# @log_function
# def add(a,d):
#     print( a+d)
