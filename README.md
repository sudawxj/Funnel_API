# Funnel_API
 ![this is an image](image/API.png)


This API takes an email as input and output the topic of it.

## Description

The model consists two steps:
* step 1: Topic Modeling using LDA. Inputs are unlabeled unstructured emails (emails not included in this public repo due to privacy concern). Emails are grouped into 4 topics: "TIME";"COMPUTER";"INFORMATION";"SPORTS". Each email is then labeled with one of the four topics.
* step 2: Multiclass classification using Xgboost. The model is trained with the emails as independent variable and their corresponding topics as dependent variable. The trained classifer to detect the topic of a new email. \
\
The details of the modeling steps and results can be found in [notebook](001_model/Funnel_model_building.ipynb)

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```
