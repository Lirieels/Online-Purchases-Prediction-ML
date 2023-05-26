# Machine Learning - Online Purchases Predcitions

The project will use the Online Shoppers Purchasing Intention Dataset which can be found on the link [here](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)

## Dataset 

The dataset is already preproccessed so there is no need for any preproccessing.

The dataset consists 18 columns, from which 10 are numerical and 8 are categorical. It has 12330 rows, where each row represents a different user and the actions that that user took. All the data on the dataset are collected in a year period.

### Dataset categories
The following columns are the categorical ones:
1. Month - this column is represented by the months' abbreviations
2. OperatingSystems - is represented by numbers
3. Browser - is represented by numbers
4. Region - is represented by numbers
5. TrafficType - is also represented by numbers
6. VisitorType - is represented by Returning_Visitor or New_Visitor
7. Weekend - is represented by TRUE or FALSE
8. Revenue - is represented by TRUE or FALSE

Since the columns: OperatingSystems, Region, TrafficType and VisitorType are categorized by numbers, we cannot know for sure what type of the categories these might be but we might be able to give meaning to these numbers, for example: if we take the OperatingSystems, we can say that 1 is Windows, 2 is Linux and so on.

The reason why the dataset does not show these categories are because of privacy reasons.

## Dataset preview

| Administrative | Administrative_Duration | Informational | Informational_Duration | ProductRelated | ProductRelated_Duration | BounceRates | ExitRates | PageValues | SpecialDay | Month | OperatingSystems | Browser | Region | TrafficType | VisitorType          | Weekend | Revenue |
|:--------------:|:-----------------------:|:-------------:|:----------------------:|:--------------:|:-----------------------:|:-----------:|:---------:|:----------:|:-----------:|:-----:|:----------------:|:-------:|:------:|:-----------:|:--------------------:|:-------:|:-------:|
| 0              |	0                      | 0	           | 0	                    | 1              | 0	                     | 0.2	       | 0.2	     | 0          | 0            | Feb   | 1	              | 1       | 1      | 1           | Returning_Visitor    | FALSE   | FALSE   |
| 0              |	0                      | 0	           | 0	                    | 2              | 64	                     | 0	         | 0.1	     | 0          | 0            | Feb   | 2	              | 2       | 1      | 2           | Returning_Visitor    | FALSE   | FALSE   |
| 0              |	0                      | 0	           | 0	                    | 2              | 0 	                     | 0.2         | 0.2	     | 0          | 0            | Feb   | 4	              | 1       | 9      | 3           | Returning_Visitor    | FALSE   | FALSE   |
| 0              |	0                      | 0	           | 2	                    | 2.666666667    | 0.05                    | 0.14        | 0  	     | 0          | 0            | Feb   | 3	              | 2       | 2      | 4           | Returning_Visitor    | FALSE   | FALSE   |
| 0              |	0                      | 0	           | 10	                    | 627.5          | 0.02                    | 0.05        | 0  	     | 0          | 0            | Feb   | 3	              | 3       | 1      | 4           | Returning_Visitor    | TRUE   | FALSE   |

# Usage

There are two ways to use the project, either by running two samples code or by using the custom option.

## Sample one

Sample one prepares and uses the above dataset.

### Preparation of the dataset

1. All zero rows are removed from the dataset
2. Dataset is encoded using Label Encoding 
3. Dataset is oversampled to make the two classes equals
4. Dataset is normalized using Standard Scaler

### Models training

This sample uses 5 models for training; Decision Tree, Random Forest (two versions: 50 decision trees, 60 random state and 1000 decision trees, 42 random state), K-Nearest Neighbors (two versions: 1 neighbor and 5 neighbors), Linear Regression and Gaussian Native Bayes.

### Results

After running the model training a few times, here are the accuracy scores for the models:

1.	Random Forest (1000 Decision Tree, 42 Random State) – 88%
2.	K-Nearest Neighbors (1 Neighbor) – 84%
3.	Random Forest (50 Decision Trees, 60 Random State) – 82%
4.	Linear Regression – 81%
5.	K-Nearest Neighbors (5 Neighbors) – 79%
6.	Decision Tree – 76%
7.	Gaussian Native Bayes – 70%

## Sample two

Sample two has everything from sample one, but the columns Browser, VisitorType, Region, TrafficType dhe OperatingSystem were removed from it to see how it would perform.

### Results

The results using this modification of the dataset are shown below:

1.	K-Nearest Neighbors (1 Neighbor) – 85%
2.	Random Forest (1000 Decision Tree, 42 Random State) – 79%
3.	Random Forest (50 Decision Trees, 60 Random State) – 79%
4.	Linear Regression – 82%
5.	K-Nearest Neighbors (5 Neighbors) – 80%
6.	Decision Tree – 86%
7.	Gaussian Native Bayes – 57%


## Custom

The custom option lets you customize the dataset and models. It allows you to prepare the dataset, train the models and save them as files and then load those models using the dataset.

The goal of this option was to easily let you tweak the dataset and the models' parameters to see if there would be any model that would have a pretty good accuracy score.

The trained models are saved as files and then those models can be loaded later.

### Prepare dataset

The prepare option lets you preprocess the dataset. It has three options:

1. Remove zero rows - it removes the rows where all columns are zero
2. Encoding - it lets you encode the dataset using Label Encoding and Hot-One Encoding
3. Normalize - it lets you normalize the dataset using Standard Scaler

### Train models

This option lets you train the models mentioned above. It lets your custom inputs for the models' parameters (if supported) then it saves those trained models into files.

### Load models

This option lets you load trained models and predict the results using those models with the provided dataset.

# Project

The project will be developed using Python.
The goal of this project is that by using the dataset, we would predict the online purchases that a user would make if he took different combination of actions.

# Notes

The information here are not final and will be updated frequently until the project is finished completely.

# About

This project is being developed as a project work of the "Machine Learning" course by two students of Unviersity of Prishtina. 
