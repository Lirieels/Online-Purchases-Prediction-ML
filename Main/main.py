import os
import prepare as prepare
import train as train
import models as models
import sample as sample

def options_selector(data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------\n')

    print('Options:')
    print('1. Sample')
    print('2. Custom')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if(option==1 or option==2):
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")

    if(option==1):
        sample.use_sample()
    elif(option ==2):
        custom_options_selector(data)


def custom_options_selector (data):
    os.system('cls||clear')
    print('-------------------------------------------------------------------------------')
    print('--------------------------Online Purchases Predictions-------------------------')
    print('-------------------------------------------------------------------------------\n')

    print('Options:')
    print('1. Prepare dataset')
    print('2. Train models')
    print('3. Load models')
    while True:
        try:
            option = int(input('Please enter one option from above: '))
            if(option==1 or option==2 or option == 3):
                break
            print("That's not a valid option!")
        except:
            print("That's not a valid option!")

    if(option==1):
        prepare.prepare_options(data)
    elif(option ==2):
        train.train_options()
    elif(option ==3):
        models.load_models()
