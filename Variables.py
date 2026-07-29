# Local variable
def display():
    x = 10   
    print("Local Variable:", x)

display()




# Global variable
x = 20   

def display():
    print("Global Variable:", x)

display()
print(x)



# Instance variable
class Student:
    def __init__(self):
        self.name = "Rohit"   

s = Student()
print(s.name)




# Class variable
class Student:
    college = "ABC College"   

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)
