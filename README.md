> # DESCRIPTION
This is a capstone level classification ML project for predicting IPL team finishing position for an year based on Individual player's performance. The project includes web-scraping ESPN cricinfo website for ipl player statistics, pre-processing the data, and comparing different classification models and hyperparameter tuning them.

__CLASSIFICATION MODELS BEING COMPARED__<br>

__*__ Models to be created include __KNN, Logistic Regression, Decision Tree , Random Forest, SVM, Naive Bayes__

#### Classification Capstone Project Tasks
- Identifying a domain with a problem which can be addressed using Prediction Techniques.
- Creating a Dataset for classification with minimum 20 Features and 100 rows. The Data is scrapped from espn cricinfo's website.
- Ensure the dataset has all possible combination of feature where data preprocessing techniques can be applied ( Data Cleaning, Dimensionality Reduction, Data Transformation, Feature Engineering).
- Applying all the categories of classification algorithm( KNN, Logistic Regression, Decision Tree, Random Forest, SVM, Naïve Bayes) along with hyper parameter tuning and measure through best suited evaluation metric.
- Using the ROC curve to determine the best algorithm for your dataset.

---
> # REPOSITORY STRUCTURE

The repository structure is highlighted below:

1. The __Webscrapping Espncricinfo IPL Stats__ folder, has ```scrape_espn_cricinfo.py```, which consists of all the functions and the ```driver_code_webscrape_ipl_dataset.ipynb``` that has the driver code for creating the player statistics dataset, through webscrapping the ESPN cricinfo website.
2. The __Extra Unused IPL Data__ folder has the salaries of each of the IPL players listed down from 2009 to 2023, this data was discarded from being used in the model, at early stages.
3. The __Final Model Building__ folder has the ```classification_models_building.ipynb``` which has all the classification models running on the pre-processed (PCA) dataset.
4. The __Data Preprocessing__ has the ```classification_models_building.ipynb``` notebook which has an extensive cleaning, pre-processing, feature engineering and dimiensionality handing within it for the Espn IPL dataset.

__Directory Tree Structure__
```bash
|____Webscrapping Espncricinfo IPL Stats
| |____driver_code_webscrape_ipl_dataset.ipynb
| |____scrape_espn_cricinfo.py
| |____batting_scrape_sample.png
| |____team_timelines.png
| |____uncleaned_dataset.csv
| |____bowling_scrape_sample.png
| |____Finishing_Position_IPL.csv
| |____README.md
|____Extra Unused IPL Data
| |____IPL Salaries
| | |____2009_IPL_Salary..csv
| | |____2010_IPL_Salary..csv
| | |____2017_IPL_Salary.csv.csv
| | |____2019_IPL_Salary.csv.csv
| | |____2016_IPL_Salary.csv
| | |____2015_IPL_Salary.csv
| | |____2021_IPL_Salary.csv.csv
| | |____2008_IPL_Salary.csv
| | |____2011_IPL_Salary..csv
| | |____2014_IPL_Salary..csv
| | |____2020_IPL_Salary.csv.csv
| | |____2013_IPL_Salary..csv
| | |____2018_IPL_Salary.csv.csv
| | |____2012_IPL_Salary..csv
| | |____2023_IPL_Salary.csv
|____Final Model Building
| |____classification_models_building.ipynb
|____Data Preprocessing
| |____data_preprocessing_notebook.ipynb
| |____pre_processed_dataset.csv
|____requirements.txt
```

---

> # DATA COLLECTION (WEBSCRAPING) 

__URL Adjustments being made for Web-Scrapping (scrape_espn_cricinfo.py)__<br>

#### Sample ESPN CRICINFO URL
**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
- Batting: https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament
- Bowling:https://stats.espncricinfo.com/ci/engine/records/bowling/most_wickets_career.html?id=3519;team=4340;type=tournament

### Note: Exceptions
These following teams are either new entrants, defunct, or were suspended in between seasons, so upon trying to webscrape the following, we will be thrown an error or will receive an empty dataset.<br>
1. **Decan Chargers**
2. **Pune Warriors India** 
3. **Kochi Tuskers Kerala**
4. **Gujarat Lions**
5. **Rising Pune Supergiants**
6. **Lucknow Super Giants**
7. **Gujarat Titans**
8. **Chennai Super Kings**
9. **Rajasthan Royals**


![team_timelines](https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/6659fbda-9d8a-4366-bb91-1fb2e4266ae2)

To handle this abnormality, we created nested dictionaries in the ```scrape_espn_cricinfo.py``` webscrapping file that hold the team's id assigned in the ESPN Cricinfo database and the years they have participated in the IPL in. These years will then be iterated through to avoid discrepencies

---
## Scrapping IPL batting stats from ESPN cricinfo

### 1. scrape_batting_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__

![batting_scrape_sample.png](attachment:batting_scrape_sample.png)

**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament

### 1. scrape_batting_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__<br>

<img width="1438" alt="batting_scrape_sample" src="https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/13ea6500-bd24-4ec1-884b-e0ae8f181739">

**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=3519;team=4340;type=tournament


### 2. create_batting_stats_dataset()
Function to iterate through all the teams and years, and create the batting dataset by calling the "scrape_batting_stats_espn()" function created earlier.

---

## Scrapping IPL bowling stats from ESPN cricinfo

### 1. scrape_bowling_stats_espn()
Function to request to espncricinfo stats teamwise, yearwise page and scrape relevant information and add to a temporary dataset.<br>
__Screenshot of a sample page to be web-scrapped:__

<img width="1430" alt="bowling_scrape_sample" src="https://github.com/shreyansh-2003/IPL-Team-Finishing-Position-Prediction-Project/assets/105413094/30357b24-9d1b-4b0c-aa11-a395a5f9f096">


**Year: 2008<br> Team: Royal Challengers Bangalore**<br>
https://stats.espncricinfo.com/ci/engine/records/bowling/most_wickets_career.html?id=3519;team=4340;type=tournament

### 2. create_bowling_stats_dataset()
Function to iterate through all the teams and years, and create the batting dataset by calling the "scrape_bowling_stats_espn()" function created earlier.


> # Data Pre processing

Some of the techniques applied within data pre-processing are:
1. __Handling NA values__: After analyzing the missing values for both batting and bowling columns, I have found that if a player has not batted or bowled in a particular season, all of their corresponding batting and bowling columns have missing values. Hence, it is reasonable to assume that these missing values are not actual values but rather an indication that the player did not bat or bowl in those matches. Therefore, I will fill all of these missing values with 0, which is a common practice in such cases, and an accurate depiction.
2. __Adding new columns__
3. __Data Type Casting__
4. __Ordinal Encoding__
5. __Label Encoding__
6. __Robust Scaling__
7. __PCA (Principal Component Analysis)__

> # Classification Models

__Hypothesis:__ Winning or success rate in a team sport like cricket, football does not entirely depend on the individual performance of the player, rather a team wins or performs well when most of the players of that team plays exceptionally good.<br>

The calssification models used (from sci-kit learn) in tandem for the project include:
1. __KNN__ (KNeighborsClassifier)
2. __Random Forest__ (RandomForestClassifier)
3. __Decision Tree__ (DecisionTreeClassifier)
4. __Logistic Regression__ (LogisticRegression)
5. __Naive Bayes__ (GaussianNB)
6. __SVM__ - Support Vector Machine (SVC)

GridSearch CV is used for extensive hyperparameter tuning.
