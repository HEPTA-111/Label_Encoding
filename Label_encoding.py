# Import libraries 
import numpy as np 
import pandas as pd 


# Import label encoder 
from sklearn import preprocessing 

# Import dataset 
df = pd.read_csv('data/Iris.csv') 

df['Species'].unique()



# label_encoder object knows  
# how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
  
# Encode labels in column 'Species'. 
df['Species']= label_encoder.fit_transform(df['Species']) 
  
df['Species'].unique()



