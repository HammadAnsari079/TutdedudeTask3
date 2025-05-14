def fac():
    n = int(input("Enter tany number: "))
    Factorial = 1
    if n == 1:
        print("Fcatorial is 1")
    for i in range(2,n+1):
        Factorial *= i
    print("The Factorial of",n,"is",Factorial)

fac() 