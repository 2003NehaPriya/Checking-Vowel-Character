#check given input(char) is vowel or not
a=input("vowel, or 9 to quit: ")
b=["a","e","i","o","u","A","E","I","O","U"]
c=['1','2','3','4','5','6','7','8','0']
while True:
    if(a in b):
        print("vowel")
    elif(a in c):
        print("wrong input")
    elif(a=='9'):
        break
    else:
        print("not vowel")
    a=input("vowel, or 9 to quit: ")

    
