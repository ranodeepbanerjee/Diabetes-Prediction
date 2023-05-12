# Diabetes-Prediction
Live webapp link: https://ranodeepbanerjee-diabetes-prediction.streamlit.app/<br>
Kaggle notebook link: https://www.kaggle.com/ranodeepbanerjee/diabetes-prediction<br>

Sample input values to try the web app: 2	197	70	45	543	30.5	0.158	53 

## Introduction
This is a machine learning project that aims to predict whether a person has diabetes or not based on certain diagnostic measurements. The dataset used for this project is the [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), which contains diagnostic measurements for 768 women of Pima Indian heritage.

## Technologies Used
This project was implemented using Python programming language and the following libraries:<br>

* NumPy
* Pandas
* Scikit-learn

## Data Collection and Analysis
The Pima Indians Diabetes Database was collected from the National Institute of Diabetes and Digestive and Kidney Diseases. It contains eight diagnostic measurements, including the number of pregnancies the patient has had, their glucose levels, blood pressure, skin thickness, insulin levels, body mass index (BMI), diabetes pedigree function, and age.<br>

To analyze the dataset, we used Pandas to load the data and explored the dataset using various statistical measures such as mean, standard deviation, and quartile range. We also visualized the dataset using various charts and graphs to get a better understanding of the data.

## Data Preprocessing
Before building the machine learning model, we need to preprocess the dataset. We performed the following preprocessing steps:

* Splitting the dataset into the input features (X) and target variable (Y).
* Standardizing the input features using Scikit-learn's StandardScaler to scale the features to have zero mean and unit variance.
## Machine Learning Model
We used Support Vector Machine (SVM) to build our machine learning model. SVM is a supervised learning algorithm that can be used for both classification and regression tasks. SVM works by finding the best hyperplane that separates the data into different classes.<br>

We split the preprocessed dataset into training and testing sets, trained the SVM model on the training set, and evaluated its performance on the testing set using accuracy as the evaluation metric.

## Results
After training the SVM model on the preprocessed dataset, we achieved an accuracy of 79.17% on the testing set. This means that our model correctly predicted the diabetes status of 79.17% of the patients in the testing set.

## Conclusion
In this project, we used machine learning techniques to predict the diabetes status of patients based on certain diagnostic measurements. We achieved an accuracy of 79.17% on the testing set, which is a good start, but there is still room for improvement. Future work can focus on feature selection, hyperparameter tuning, and trying out different machine learning algorithms to improve the accuracy of the model.
