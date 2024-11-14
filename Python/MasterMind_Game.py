
import random
COLORS=["R","G","B","Y","W","O"]
TRIES=10
CODE_LENGTH=4


def generate_code():

    code=[]
    for _ in range(CODE_LENGTH):
        color=random.choice(COLORS)
        code.append(color)
    print(code)
    return code


def guess_code():

    while True:

        guess=input("Guess:").upper().split(" ")
        #"G G G G" -> ["G","G","G","G"]

        if len(guess)!=CODE_LENGTH:
            print(f"You  Must guess {CODE_LENGTH} Colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color:{color}. Try Agian")
                break
        else:
            break

    return guess


def check_code(guess,real_code):

    color_count={}
    correct_pos=0
    incorrect_pos=0

    for color in real_code:
        if color not in color_count:
                color_count[color]=0
        color_count[color]+=1

        # guess=["G","R"]
        # real=["W","Y"]
        # [("G","W") , ("R","Y")]

    for guess_color , real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_pos+=1
            color_count[guess_color]-=1
    

    for guess_color , real_color in zip(guess,real_code):

        if guess_color in color_count and color_count[guess_color]>0:
            incorrect_pos+=1
            color_count[guess_color]-=1

    return correct_pos , incorrect_pos


def game():

        code=generate_code()

        for attempts in range(1,TRIES+1):

            guess=guess_code()
            correct_pos,incorrect_pos=check_code(guess,code)

            if correct_pos == CODE_LENGTH:
                print(f"You Guessed the Code in {attempts} Tries!")
                break

            print(f"Correct Positions:{correct_pos} | Incorrect Positions:{incorrect_pos}")

        else:
            print(f"You ran out of Tries,the code was:",*code)

    
if __name__ =="__main__":
     print("|--------------------------------------------------|   Welcome to the MaterMind Game   |----------------------------------------------|\n")
     game()

