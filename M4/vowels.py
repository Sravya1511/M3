X = input("Enter a string")
C = 0
for letter in X:
    if letter in ('a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U'):
        C = C+1
print("Number of vowels:"+ str(C))        