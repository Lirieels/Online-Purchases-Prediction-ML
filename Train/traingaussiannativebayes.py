from sklearn.naive_bayes import GaussianNB
import dataset as dataset
import directory as directory
import pickle
from datetime import datetime


def train(data):
    train, valid, test = dataset.split_train_valid_test(data)
    train_data, X_train, y_train = dataset.split(train)
    gnb_model = GaussianNB()
    print("Please wait while the model is being trained.")
    gnb_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    directory_path = "Models/GaussianNativeBayesModels/"
    directory.make_directory(directory_path)
    filename = directory_path+"Gaussian_Native_Bayes_Model" + dt_string + ".sav"
    pickle.dump(gnb_model, open(filename, 'wb'))
    print("Gaussian Native Bayes model has been trained!")