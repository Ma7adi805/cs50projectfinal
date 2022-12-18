#library
import time
import random

#variables
coin = 10
level = 1
run = True
name="unkown"

#functions
#checks the players coin
def check_coin():
    global coin
    print("You have", str(coin), "coins \n would you like to buy more")
    #asks if player want to purchase more coins
    check_coin_input_for_purchase = input("Would you like to purchase more? ")
    check_coin_input_for_purchase_upper = check_coin_input_for_purchase.upper()
    if check_coin_input_for_purchase_upper=="YES" or check_coin_input_for_purchase_upper=="Y":
        print("\n \t Shop \n\n \t 5 Coins For $10 \t 10 coins for $20 \t 50 coins for $50")
        player_decides_to_purchase = input("\n What would you like to purchase? ")
        if player_decides_to_purchase=="5":
            print("Purchasing")
            print("Checking If approved payed")
            time.sleep(2)
            print("Approved")
            coin1 = coin+5
            coin=coin1
            print("You now have",str(coin),"coins")
        elif player_decides_to_purchase=="10":
            print("Purchasing")
            print("Checking If approved payed")
            time.sleep(2)
            print("Approved")
            coin1 = coin+10
            coin=coin1
            print("You now have",str(coin),"coins")
        elif player_decides_to_purchase=="50":
            print("Purchasing")
            print("Checking If approved payed")
            time.sleep(2)
            print("Approved")
            coin1 = coin+50
            coin=coin1
            print("You now have",str(coin),"coins")
    else :
        print("Going Back To Main Page.. \n")

def account_setup():
    global name
    print("Setting Up Account")
    time.sleep(1)
    print("Hello User, What is your name")
    playernameinput=input("")
    if playernameinput=="":
        print("Name Cannot Be used")
        print("Reloading")
        time.sleep(1)
        account_setup()
    else:
        name=playernameinput

def play():
    global coin
    levelchoose=input("Which Level Would You Like to play \n Easy \t Normal \t Medium \t hard \n").lower()
    #level easy
    if levelchoose=="easy":
        choosen_num=str(random.randint(1,5))
        print(choosen_num)
        print("choosen_num")
        print("Choose A Number Between 1 and 5 \n For Hint Type \"H\"")
        player_choice=input().lower()
        if player_choice=="h":
            print("The Value is nearly", str(int(choosen_num)+random.randint(1,2)))
            print("Choose A Number Between 1 and 5")
            player_choice=input().lower()

            if player_choice.isnumeric():
                print("You entered Value", player_choice)
                time.sleep(1.5)
                print("Checking")
                if player_choice==choosen_num:
                    print("You have won \n5 coins have been added to your account")
                    coin1 = coin+5
                    coin=coin1
                    print("You now have", coin,"coins")

                else:
                    coin_to_give = str(random.randint(1,3))
                    print("The Number was", choosen_num)
                    print("Sorry You have lost \n We will give you",coin_to_give,"coins for trying")
                    coin=coin+int(coin_to_give)
            else:
                print("ERROR 404 Looks like your input is not an integer")
                print("Reloading To THe Game")
                play()

        elif player_choice.isnumeric():
            print("You entered Value", player_choice)
            time.sleep(1.5)
            print("Checking")
            if player_choice==choosen_num:
                print("You have won \n 5 coins have been added to your account")
                coin1 = coin+5
                coin=coin1
                print("You now have", coin,"coins")

            else:
                coin_to_give = str(random.randint(1,3))
                print("The Number was", choosen_num)
                print("Sorry You have lost \n We will give you",coin_to_give,"coins for trying")
                coin=coin+int(coin_to_give)
        else:
            print("ERROR 404 Looks like your input is not an integer")
            print("Reloading To THe Game")
            play()
    else:
        print("ERROR 404 Level Not Available")



commands_func= {'check_coin':check_coin,'play':play}
cmds= ('check_coin, play, exit')
while run:
    if name=="unkown":
        account_setup()
    else:
        print("Hello",name+", Welcome to Number Guessing Here are the following commands,",cmds)
        whattorun=input("> ")
        if whattorun=="exit":
            break
        else:
            commands_func[whattorun.lower()]()

