class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Hello my name is {self.name}. I am {self.age} years old.")

s1=student("Milan",22)
s2=student("John",34)

# Avg of list using fn
n=[4,5,7,3]
def findavg(n):
    sum=0
    for i in n:
        sum=sum+i
    print(f"Average is {sum/len(n)}")
findavg(n)


# A lambda function (also called an anonymous function) is a small function written in a single line, 
# usually when you don't want to define a full function with def. SYNTAX: lambda arguments: expression

def square(x): # normal fn
    return x * x

print(square(5))

sqre = lambda x: x * x # Lambda fn

print(sqre(7))
#  virtual env: python -m venv myenv  , activate venv : myenv\Scripts\Activate  , install numpy: pip install numpy

class std:
    pass
s3=std()
s4=std()
std.name="Milan"
std.age=22

print(f"{s4.name} is {s3.age} years old")
print(s4.age)