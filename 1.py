apple=[10,20,30,40,50]
print(apple)
print([1])
print([-1])
print("for iteration via access elements")
for i in apple:
    print(i)
print("after changed")
apple[1]=-100
print(apple)
apple[2]=(300,400)
print(apple)
print(apple[-1])
apple[3]=500,600,700
print(apple)
apple[1:4]=(-10,-20,-30)
print(apple)
    