try:
    num=int(input("enter number:"))
    assert num%2==0

    #cade that may couse expeption
except:
    print("not an even number!")
    
else:
    reciprocal=1/num
    print(reciprocal)

