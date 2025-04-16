# class animal:
#     def __init__(self):
#         pass
#     def make_sound(self):
#         print("some animal sound")
# class dog(animal):
#     def make_sound(self):
#         print("Bark")
#         return super().make_sound()
# class cat(animal):
#     def make_sound(self):
#         print("Meow")
#         return super().make_sound()
# obj=animal()
# obj.make_sound()
# obj1=dog()
# obj1.make_sound()
# obj2=cat()
# obj2.make_sound()
class student:
    def developer(self):
        print("it is developer")
class ali(student):
    def developer(self):
        print("ali is java developer")
class ahmed(student):
    def developer(self):
        print("Ahmed is python developer")
def deve(student):
    student.developer()
    
deve(ali())