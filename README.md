# Final Project of Data Science and Machine Learning Course
# Purwadhika Startup and Coding School 
## 80% of Total Population Vaccination Prediction

### Introduction
While we are in the middle of a pandemic, the progress of worldwide vaccinations has led confusion to some with many problems and one of them is the unequity of vaccines distribution. Seeing from how developed countries be able to get the vaccines first or even pre-ordered the vaccines just before it was made. Many people are wondering how long does it take to get vaccinated for all of the citizens in their country. This final project hopefully will give a general image of how long it takes to vaccinate at least 80% of total population, the prediciton itself is coming from the mean and StDev of Daily Vaccinations 

### Problem Statement
Days required to vaccinate 80% of total population

### Goals
- Identifying the unequity issue taken from how long a country get a vaccine compared to developed countries
- Finding quantitative measure that represent the factors
- Building machine learnng model to predict days required to achieve herd immunity
- Show type of vaccine(s) available 
- Connecting the prediction system into a dashboard

### Result
- Factors of herd immunity behavior includes:
  1. Mean of Daily Vaccinations, stdev of Daily Vaccinations
  2. Non-transparant issue (e.g: one day there is a vaccination progress, the next day there isn't any vaccination progress)
  3. To be at least covers 80% of total population of every countries.
  
- Quantitative measure that represents the factors:
  1. Daily Vaccinations
  2. Status of vaccine(s) variant in each country
  3. Status of vaccine(s) being utilised based on percentage
  
- Machine learning model:
  1. TimeSeries Analysis Machine Learning
  2. We are going to use 'date' and 'Daily Vaccination' as our basis column to analyze the vaccination trend. The method will be Auto Regression Integrated Moving Average (ARIMA)
  
- Dashboard
  1. Dashboard menu consists of prediction of Daily Vaccinations mean based to get the duration of Vaccination
  2. People get to know how long will it takes for their country to get vaccinated to the point of 80% of total populations, and which variant of vaccines are currently being utilised by their government

### Recommendation
1. The government could speed-up the vaccinations progress to their people, seeing how many lives the disease has taken
2. For the world to unite to end the plague, because if there is still an unequity in regards to the distribution of the vaccines, none in any world, we will get out of this dark moment. The data supported on how lack the vaccinations in South Africa that it ended up having mutations that some vaccines are not effective in some countries with severe diseases.


### Note
Although we some how kind of predict the timeline, the virus will still be able to mutate in the future and require some boosts from vaccines manufacturer. At this point, new data is required, then the prediction is basically useless. 

