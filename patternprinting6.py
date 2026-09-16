for i in range(5):
    print("*")

for i in range(6):
    print("#") 

# printing verticallty
for i in range(10):
    print(i)
# printing horizontally
for i in range(11):
    print(i,end="    ")

# printing row and column wise
for i in range(6):
    for j in range(6):
        print(i,end="  ")
    print()

for i in range(6):
    for j in range(6):
        print(j,end="  ")
    print()