# CZ4032-Data-Mining-and-Analytics

### Setup virtual environment in project

In Windows CMD, ensure you are in the folder of your repository

1. Run `python –m venv venv`
2. Run `venv\Scripts\activate` 
3. Run `pip install -r requirements.txt`

All required packages should have been installed!

`venv\Scripts\activate` is also the <b>command to enter your virtual environment</b> whenever you want to run the application on CMD


### Instruction Guide to read the files

### Part 2: Association Rule Mining & Building of Classifier (CBA)

To run: `association_rule\association_rule.py` and replace the code in lines 12 to 19 (stated below) with respect to the dataset

#### 1) Breast Cancer: "diagnosis" (min_support = 0.05)

```
DATA_SOURCE = 'BreastCancer\data.csv'

attributes = [
'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
'smoothness_mean', 'compactness_mean', 'concavity_mean',
'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst',
'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst',
'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst','diagnosis'
]

attribute_to_classify = 'diagnosis'
```

#### 2) Bank Marketing: "Subscribed" (min_support = 0.3)

```
DATA_SOURCE = 'BankMarketing\bank.csv'

attributes = [
'age','job','marital','education','default','balance',
'housing','loan','contact','day','month','duration',
'campaign','pdays','previous','poutcome','Subscribed'
]

attribute_to_classify = 'Subscribed'
```

#### 3) Forest Fire: "Classes" (min_support = 0.1)

```
DATA_SOURCE = 'ForestFires\Algerian_forest_fires_dataset_UPDATE.csv'

attributes = [
'day','month','year','Temperature','RH','Ws','Rain',
'FFMC','DMC','DC','ISI','BUI','FWI','Classes'  
]

attribute_to_classify = 'Classes'
```

#### 4) Heart_Failure: "DEATH_EVENT" (min_support = 0.1)

```
DATA_SOURCE = 'HeartFailure\heart_failure_clinical_records_dataset.csv'

attributes = [
'age','anaemia','creatinine_phosphokinase','diabetes,ejection_fraction',
'high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex',
'smoking','time','DEATH_EVENT'
]

attribute_to_classify = 'DEATH_EVENT'
```

#### 5) adult_cleaned: "income" (min_support = 0.2)

```
DATA_SOURCE = 'Adults\data_cleaned.csv'

attributes = [
'age','workclass','fnlwgt','education','education-num',
'marital-status','occupation','relationship','race','sex',
'capital-gain','capital-loss','hours-per-week','native-country',
'income'
]

attribute_to_classify = 'income'
```

#### 6) Occupancy: "Occupancy" (min_support = 0.05)

```
DATA_SOURCE = 'Occupancy\data.csv'

attributes = [
'Temperature','Humidity','Light','CO2','HumidityRatio','Occupancy'
]

attribute_to_classify = 'Occupancy'
```

#### 7) Wine: "Quality_enc" (min_support = 0.05)

```
DATA_SOURCE = 'Wine\wine.csv'

attributes = [
'fixed_acidity','volatile_acidity','citric_acid',
'residual_sugar','chlorides','free_sulfur_dioxide',
'total_sulfur_dioxide','density','pH','sulphates',
'alcohol','quality'
]

attribute_to_classify = 'quality'
```

### Part 4: Other Classifiers

We have separated 7 datasets into 7 folders named after each respective dataset.
To run: Open the `classification.ipynb` file for your preferred dataset

### Part 5: Improvement to CBA

Similar to Step 2, but run: `association_rule\association_rule_improved.py` instead

