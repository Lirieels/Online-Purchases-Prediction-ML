import os
import main as main
import traindecisiontree as train_decision_tree


def train_options(data):
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
            if option == 0:
                main.custom_options_selector(data)
            if option == 1:
                train_decision_tree.train(data)
            elif option == 2 or option == 0:
                train_decision_tree.train(data)
        except Exception as e:
            print("That's not a valid option!" + str(e))
