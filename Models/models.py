import os
import main as main


def load_models():
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------')
    print('-----------------------------------Load models---------------------------------')
    print('-------------------------------------------------------------------------------\n')
    print('Models:')
    print('1. K-Nearest Neighbors')
    print('2. Decision Tree')
    print('3. Random Forest Tree')
    print('4. Gaussian Native Bayes')
    print('5. Linear Regression')
    print('0. Go to home')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if(option==1 or option==2 or option ==0):
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")

    if(option==0):
        main.options_selector()
