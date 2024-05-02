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

conn= connect('ecsel_database.db')
df_project= pd.read_sql ('SELECT * FROM PROJECTS', conn)
df_participants= pd.read_sql ('SELECT * FROM PARTICIPANTS', conn)
df_countries= pd.read_sql ('SELECT * FROM COUNTRIES', conn)
df2= pd.read_sql ('''SELECT p.*, pj.*, c.Country FROM PARTICIPANTS AS p, PROJECTS AS pj, COUNTRIES AS c
WHERE p.projectID=pj.projectID AND p.country=c.Acronym''', conn)
df2=df2.rename(columns={'country':'Acronym'})
df2=df2.rename(columns={'acronym':'organization_acronym'})

#hola vale creo que si se usa esto funciona:
#df3 = df2.copy()
#for col in df2.columns:
   # df3[col] = df3[col].astype(str)

"""Part 3:"""

country_list = df2['Country'] #selecting the country names list
country_acronyms = {'Belgium': 'BE', 'Bulgaria': 'BG', 'Czechia': 'CZ', 'Denmark': 'DK', 'Germany':
'DE', 'Estonia': 'EE', 'Ireland': 'IE','Greece': 'EL', 'Spain': 'ES', 'France': 'FR', 'Croatia':
'HR', 'Italy': 'IT', 'Cyprus': 'CY', 'Latvia': 'LV', 'Lithuania': 'LT','Luxembourg': 'LU',
'Hungary': 'HU', 'Malta': 'MT', 'Netherlands': 'NL', 'Austria': 'AT', 'Poland': 'PL', 'Portugal':
'PT','Romania': 'RO', 'Slovenia': 'SI', 'Slovakia': 'SK', 'Finland': 'FI', 'Sweden': 'SE'}
countname = st.selectbox('Choose a Country', country_acronyms.keys()) #input by the user of the name of the country
def country_to_acronym(countname): #defining a function
  found = False #setting parameter = False, when True it is when the acronym is found.
  while found == False: #while acronym is not found
    if countname in country_acronyms.keys(): #if the country name is in the key of the dictionary
      value = country_acronyms[countname] #getting the acronym associated with the key (name of the country)
      found = True #set parameter to trye
    else:
      st.write("Not a country on the list, try again: ") #if the country doesn't exist in the database it will ask the user again to try again
      found = False
    return(value)

acronym_c = country_to_acronym(countname)
st.write('The selected country is:', acronym_c) #calling the function to display to display the acronym 


@st.cache
def display_dataframe(df2, acronym_c):
    df2 = df2[df2['Acronym'] == acronym_c]
    df2_part = df2.groupby(['name','shortName', 'activityType', 'organizationURL']).agg({'ecContribution':['sum']})
    return(df2_part)

participants = display_dataframe(df2,acronym_c)
st.write(participants)

conn.close()

