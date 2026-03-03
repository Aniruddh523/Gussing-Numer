'''
IMP NOTE ABOUT THIS TOPICS 
o chek the guessing leve game 
if you want to exit the game to shift+z to exit the game 
 '''
import random
store =random.randint(1,100)
while True:
    inp=int(input("enter the number here to chek you are(1to100)"))
    if(inp < store):
        print("enter big value ")
    elif(inp>store):
        print(" enter less value you are closer ")
    elif(inp==store):
        print("\n yoooooooo you guess the correct you won now \n😁😍😍😍")
         

    
