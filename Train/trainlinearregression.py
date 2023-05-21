from sklearn.linear_model import LinearRegression
import dataset as dataset
import directory as directory
import pickle
from datetime import datetime


def train(data):
    train, valid, test = dataset.split_train_valid_test(data)
    train_data, X_train, y_train = dataset.split(train)
    lr_model = LinearRegression()
    print("Please wait while the model is being trained.")
    lr_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    directory_path = "Models/LinearRegressionModels/"
    directory.make_directory(directory_path)
    filename = directory_path+"Linear_Regression_Model" + dt_string + ".sav"
    pickle.dump(lr_model, open(filename, 'wb'))
    print("Linear Regression model has been trained!")