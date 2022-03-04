## parser functions ideas are from https://www.youtube.com/watch?v=cdblJqEUDNo
## Python Tutorial - Argparse by Johnny Metz

## import pands library as ps
import pandas as pd
import argparse
import datetime

## create DataFrame from owid-covid-data.csvhttps://covid.ourworldindata.org/data/owid-covid-data.csv
## there 2 ways to access dataset, 1st one is use link
## df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', encoding = 'ISO-8859-1')
## this code choosed the 2nd way as show below.
df = pd.read_csv('owid-covid-data.csv', encoding = 'ISO-8859-1')

## extract useful column based on the parta1 requirement
df = df[['location','date','total_cases','new_cases','total_deaths','new_deaths']]

df['date'] = pd.to_datetime(df['date'])
## get date in year 2020
df=df[df['date'].dt.year == 2020]
## get month from df date
df['month'] = pd.DatetimeIndex(df['date']).month
## format month as 01 02 03...12
df['month'] = df.month.map("{:02}".format)

## delete no entries for certain combinations of locations and months.
df = df.dropna(axis = 0, subset=['location'])
df = df.dropna(axis = 0, subset = ['month'])

df =df[['location','month','total_cases','new_cases','total_deaths','new_deaths']]

## aggreate total_cases, new_cases, total_deaths, new_deaths from DataFrame.
## monthly total_case max is this monthly total case
## sum new_cases for monthly total new ceses
## total deaths logic as same as total case
## new deaths logic as same as new cases
df = df.groupby(['location','month'],as_index=False).agg({'total_cases':'max','new_cases':'sum','total_deaths':'max','new_deaths':'sum'})

## caculate fatality rate
df['case_fatality_rate'] = df['new_deaths']/df['new_cases']


## sort the rows by location and month in ascending order
df = df.sort_values(['location','month'],ascending = [True,True])

## rearrange the df columns
df = df[['location','month','case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]

## get command line arugument 
parser = argparse.ArgumentParser()
parser.add_argument("filename")
agrs = parser.parse_args()

## print the first 5 rows of the final dataframe.
print(df.head().to_string(index = False))

## create .csv file to store the final result based on the command line argument
df.to_csv(agrs.filename,index = False)

