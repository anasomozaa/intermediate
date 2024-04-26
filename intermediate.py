# -*- coding: utf-8 -*-
"""intermediate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xcwSDc7AjZBrNyVb_W-vdq5YyTkS-Fpc
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot
import sqlite3

from sqlite3 import connect


import streamlit as st

excel_files= ['projects.xlsx', 'participants.xlsx', 'countries.xlsx']
dataframes= [pd.read_excel(file)for file in excel_files]

conn= sqlite3.connect('ecsel_database.db')
for df, file_name in zip(dataframes, excel_files):
  table_name=file_name.split('.')[0]
  df.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()

conn= connect('ecsel_database.db')
df_project= pd.read_sql ('SELECT * FROM PROJECTS', conn)
df_participants= pd.read_sql ('SELECT * FROM PARTICIPANTS', conn)
df_countries= pd.read_sql ('SELECT * FROM COUNTRIES', conn)
df2= pd.read_sql ('''SELECT p.*, pj.*, c.Country FROM PARTICIPANTS AS p, PROJECTS AS pj, COUNTRIES AS c
WHERE p.projectID=pj.projectID AND p.country=c.Acronym''', conn)
df2=df2.rename(columns={'country':'Acronym'})
df2=df2.rename(columns={'acronym':'organization_acronym'})
#conn.close()

"""Part 3:"""

#conn = connect('ecsel_database.db')
country_list = df2['Country']

option = st.selectbox('Choose an option', [{'Belgium': 'BE', 'Bulgaria': 'BG', 'Czechia': 'CZ', 'Denmark': 'DK', 'Germany':
'DE', 'Estonia': 'EE', 'Ireland': 'IE','Greece': 'EL', 'Spain': 'ES', 'France': 'FR', 'Croatia':
'HR', 'Italy': 'IT', 'Cyprus': 'CY', 'Latvia': 'LV', 'Lithuania': 'LT','Luxembourg': 'LU',
'Hungary': 'HU', 'Malta': 'MT', 'Netherlands': 'NL', 'Austria': 'AT', 'Poland': 'PL', 'Portugal':
'PT','Romania': 'RO', 'Slovenia': 'SI', 'Slovakia': 'SK', 'Finland': 'FI', 'Sweden': 'SE'}])
