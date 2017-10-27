#Morgan Baughman
#10/27/17
#warmUp.py - figure out the GCF of two numbers


def GCF(num1,num2):
    for i in range(num1,0,-1):
        if num1%i == 0 and num2%i == 0:
            return(i)

print(GCF(10,15))