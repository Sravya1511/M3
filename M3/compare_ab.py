"""Numbers"""
VA = input("Enter value")
VB = input("Enter value")
if VA.isalpha() or VB.isalpha():
    print("string involved")
else:
    A = int(VA)
    B = int(VB)
    if A > B:
        print("bigger")
    elif A < B:
        print("smaller")
    elif B == A:
        print("equal")
