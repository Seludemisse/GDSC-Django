character = input("Please Entern the pattern to be printed : ")

if character.lower() in ['a','e','i','o','u']:
    print("Vowels are not allowed in the input")
elif len(character)>1:
    print("The length of the character should be 1")

else:    

 for x in range(1,6):
    if x==1:
        print(character)
    elif x==2:
        print(character*2)
    elif x==3:
        print(character*3)
    elif x==4:
        print(character*4)
    elif x==5:
        print(character*5)