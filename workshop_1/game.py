 # 2.  Let’s play “Guess The Number Game”.
 # Generate randominteger in range (0,20) and then try to guess it with console input.
 # 1.If “” or “exit” entered, program will exit
 # 2.If no digital was entered, show appropriate messageand wait for new input
 # 3. If entered number greater than generated one, showappropriate message
 # 4.If entered number lower than generated one, showappropriate message

import random
def main():
    guessingNum = random.randint(0, 20)
    num = input("Enter an integer from 0 to 20:")
    print(guessingNum)

    while num:
        if num.isdigit():
            if int(num) > guessingNum:
                print ("number is greater")
                num = input("Enter an integer from 0 to 20:")
            elif int(num) < guessingNum:
                print ("number is lower")
                num = input("Enter an integer from 0 to 20:")
            else:
                print("ok")
                break
        else:
            if num == "exit":
                break
            else:
                print ("not corrct, try to enter digital number!!!")
                num = input("Enter an integer from 0 to 20:")


if __name__ == '__main__': main()
