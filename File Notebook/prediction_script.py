# basic library
import numpy as np
import pandas as pd

# model
import pickle

# load Data
df_data_testing = pd.read_csv(r"bank-additional.csv")
df_data_testing['job'] = df_data_testing['job'].replace("admin.", "admin")

# load Model
filename = r"term_deposit_prediction.sav"
loaded_model = pickle.load(open(filename,'rb'))

y_pred = loaded_model.predict(df_data_testing)
df_data_testing['y'] = np.where(y_pred == 1, 'yes','no')

df_data_testing.to_csv('prediction result.csv')