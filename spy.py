
#spy game
#return false if the sequence doesn't match [0,0,7] 
def game(num):
    c=[]
    for i in num:
        if(i==0):
            c.append(i)
        elif(i==7):
            c.append(i)
    return c==[0,0,7]
num=[1,2,0,7,9,0,7,6,7,0]
print(game(num))
