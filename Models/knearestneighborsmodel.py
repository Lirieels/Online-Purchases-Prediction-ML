import directory as directory
import loadmodel as load_model

def get_models(data):
    directory_path = "Models/KNearestNeighborsModels/"
    files = []
    if directory.directory_exists(directory_path):
        files = directory.list_files(directory_path)
    print('---------------------------------------------------')
    print('-----------K-Nearest Neighbors Models--------------')
    print('---------------------------------------------------')
    for index, value in enumerate(files):
        print(f"{index}. {value}")
    print('---------------------------------------------------')
    model_file = int(input('Please enter one model from above: '))
    load_model.model_predict(data,directory_path,files[model_file])


