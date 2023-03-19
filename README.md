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


# Project

The project will be developed using Python.
The goal of this project is that by using the dataset, we would predict the online purchases that a user would make if he took different combination of actions.

# Notes

The information here are not final and will be updated frequently until the project is finished completely.

# About

This project is being developed as a project work of the "Machine Learning" course by two students of Unviersity of Prishtina. 
