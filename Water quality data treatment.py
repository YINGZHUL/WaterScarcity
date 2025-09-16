#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Monthly water quality data


# In[2]:


# treat T data in Sep, Jun, Jul, and Feb separately because fish T requirements  
# are split by before and after 15th of these months according to fish life stages.
import pandas as pd
data = pd.read_csv('EIM_2023Aug29_13069_T.csv')
data.head()

# seperated_T_Monthly for September, June, July, Feb
data['Month'] = pd.to_datetime(data['Field_Collection_Start_Date']).dt.month
september_data = data[data['Month'] == 9]
september_data['Day'] = pd.to_datetime(september_data['Field_Collection_Start_Date']).dt.day
september_data['before15'] = september_data['Day'] <= 15
september_data['after15'] = september_data['Day'] > 15

june_data = data[data['Month'] == 6]
june_data['Day'] = pd.to_datetime(june_data['Field_Collection_Start_Date']).dt.day
june_data['before15'] = june_data['Day'] <= 15
june_data['after15'] = june_data['Day'] > 15

july_data = data[data['Month'] == 7]
july_data['Day'] = pd.to_datetime(july_data['Field_Collection_Start_Date']).dt.day
july_data['before15'] = july_data['Day'] <= 15
july_data['after15'] = july_data['Day'] > 15

feb_data = data[data['Month'] == 2]
feb_data['Day'] = pd.to_datetime(feb_data['Field_Collection_Start_Date']).dt.day
feb_data['before15'] = feb_data['Day'] <= 15
feb_data['after15'] = feb_data['Day'] > 15

#other_data = data[data['Month'] != 9]
other_data = data[~data['Month'].isin([2, 6, 7, 9])]

# other months avg
other_data_avg = other_data.groupby(['Location_ID', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 
                             'Sample_Source', 'Month']).agg({
    'Result_Value': 'mean'
}).reset_index()

# calculate monh9672 avg
september_avg = september_data.groupby(['Location_ID', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 
                             'Sample_Source', 'Month','before15']).agg({
    'Result_Value': 'mean'
}).reset_index()

june_avg = june_data.groupby(['Location_ID', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 
                             'Sample_Source', 'Month','before15']).agg({
    'Result_Value': 'mean'
}).reset_index()

july_avg = july_data.groupby(['Location_ID', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 
                             'Sample_Source', 'Month','before15']).agg({
    'Result_Value': 'mean'
}).reset_index()

feb_avg = feb_data.groupby(['Location_ID', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 
                             'Sample_Source', 'Month','before15']).agg({
    'Result_Value': 'mean'
}).reset_index()

combined_avg = pd.concat([september_avg, june_avg, july_avg, feb_avg, other_data_avg], ignore_index=True)

final_data = combined_avg[['Location_ID', 'Month', 'Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN','Sample_Source', 'Result_Value','before15']]

final_data.to_csv("T_processing9672Seperated_Monthly.csv")


# In[ ]:


# AmmoniaN, DO, Hg monthly


# In[1]:


import pandas as pd
from pathlib import Path
from glob import glob

def process_monthly_means(input_csv, date_col='Field_Collection_Start_Date'):

    df = pd.read_csv(input_csv)

    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col, 'Result_Value'])

    df['Month'] = df[date_col].dt.month

    grouped = df.groupby(['Location_ID','Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 'Sample_Source', 'Month']).agg({
        'Result_Value': 'mean'}).reset_index()

    final = grouped[['Location_ID','Calculated_Latitude_Decimal_Degrees_NAD83HARN',
                             'Calculated_Longitude_Decimal_Degrees_NAD83HARN', 'Month', 'Sample_Source', 'Result_Value']]

    in_name = Path(input_csv).name
    out_name = f"Monthly_{in_name}"

    final.to_csv(out_name, index=False, encoding='utf-8')
    return out_name
        
files = [
    'EIM_2023Oct09_13902_DO.csv',
    'EIM_2023Sep21_2997_AmmoniaN.csv',
    'EIM_2023Dec18_367_Hg.csv'
]

for f in files:
    out = process_monthly_means(f)

