from sklearn.neighbors import KNeighborsClassifier
import dataset as dataset
import directory as directory
import pickle
from datetime import datetime


def train(data):
    n_neighbors = int(input('Please enter the number of neighbors: '))
    train, valid, test = dataset.split_train_valid_test(data)
    train_data, X_train, y_train = dataset.split(train)
    knn_model = KNeighborsClassifier(n_neighbors=n_neighbors)
    print("Please wait while the model is being trained.")
    knn_model.fit(X_train, y_train)
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")
    directory_path = "Models/KNearestNeighborsModels/"
    directory.make_directory(directory_path)
    filename = directory_path+"K_Nearest_Neighbors_Model_" + dt_string + ".sav"
    pickle.dump(knn_model, open(filename, 'wb'))
    print("K-Nearest neighbors model has been trained!")