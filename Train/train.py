import os
import main as main


def train_options():
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('----------------------------------Train models---------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Algorithms:')
    print('1. K-Nearest Neighbors')
    print('2. Decision Tree')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if(option==1 or option==2 or option==0):
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")

    if(option==0):
        main.options_selector()