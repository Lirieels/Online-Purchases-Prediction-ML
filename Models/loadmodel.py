import directory as directory
import dataset as dataset
import pickle
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def model_predict(data, model_directory, model_file, extract_class=False):
    model_path = model_directory + model_file
    if directory.directory_exists(model_path):
        train, valid, test = dataset.split_train_valid_test(data)
        test, X_test, y_test = dataset.split(test)
        model = pickle.load(open(model_path, 'rb'))
        y_pred = model.predict(X_test)
        if extract_class:
            y_pred = np.where(y_pred > 0.5, 1, 0)
        score = accuracy_score(y_pred, y_test)
        print('-------------------------------------------------------------------------------')
        print(model_file)
        print('-------------------------------------------------------------------------------\n')
        print('Accuracy score: ', score, '\n')
        print('CLASSIFICATION REPORT')
        print(classification_report(y_test, y_pred))
        print('-------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------\n')
