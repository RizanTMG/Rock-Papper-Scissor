# program v2.0
# some bugs which caused errors are fixed
import random
import time
import os

a = "Rock"
b = "Paper"
c = "Scissor"

play = True
while play:
    no = random.randint(1, 3)
    print("""Choose:
        1. Rock
        2. Paper
        3. Scissor""")
    cmd = input("~>: ")
    
    try:
        cmd = int(cmd)
        # main logic
        if cmd == 1 and no == 1:
            os.system('clear')
            print('You: ' + a)
            print("Comp: " + a + '\n')
            print("Tie!")
            time.sleep(1)
        elif cmd == 1 and no == 2:
            os.system('clear')
            print('You: ' + a)
            print("Comp: " + b + '\n')
            print("You Lose!")
            time.sleep(1)
        elif cmd == 1 and no == 3:
            os.system('clear')
            print('You: ' + a)
            print("Comp: " + c + '\n')
            print("You win!")
            time.sleep(1)
        elif cmd == 2 and no == 2:
            os.system('clear')
            print('You: ' + b)
            print("Comp: " + b + '\n')
            print("Tie!")
            time.sleep(1)
        elif cmd == 2 and no == 3:
            os.system('clear')
            print('You: ' + b)
            print("Comp: " + c + '\n')
            print("You Lose!")
            time.sleep(1)
        elif cmd == 2 and no == 1:
            os.system('clear')
            print('You: ' + b)
            print("Comp: " + a + '\n')
            print("You win!")
            time.sleep(1)
        elif cmd == 3 and no == 3:
            os.system('clear')
            print('You: ' + c)
            print("Comp: " + c + '\n')
            print("Tie!")
            time.sleep(1)
        elif cmd == 3 and no == 1:
            os.system('clear')
            print('You: ' + c)
            print("Comp: " + a + '\n')
            print("You Lose!")
            time.sleep(1)
        elif cmd == 3 and no == 2:
            os.system('clear')
            print('You: ' + c)
            print("Comp: " + b + '\n')
            print("You win!")
            time.sleep(1)
        else:
            print("Enter: 1, 2, or 3!!")
    except ValueError:
        print("Enter: 1, 2, or 3!!") 
        
    print("Wanna play again(Y/N)?")
    command = input("~>")
    command = command.upper()
    
    # second logic
    if command == "N":
        print("Bye-Bye!")
        time.sleep(1)
        break
    elif command == "Y":
        os.system('clear')
        pass
    else:
        print("Enter right command next time!!")
        time.sleep(1)
        break
