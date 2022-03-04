## some are from part1a.py solutions
import pandas as pd
import argparse
import matplotlib.pyplot as plt
## create DataFrame from owid-covid-data.csv
df = pd.read_csv('owid-covid-data.csv', encoding = 'ISO-8859-1')

## extract useful column based on the parta1 requirement
df = df[['location','date','total_cases','new_cases','total_deaths','new_deaths']]
df['date'] = pd.to_datetime(df['date'])
## get date in year 2020
df=df[df['date'].dt.year == 2020]
## get year from df date
df['year'] = pd.DatetimeIndex(df['date']).year

## delete no entries for certain combinations of locations and months.
df = df.dropna(axis = 0, subset=['location'])
df = df.dropna(axis = 0, subset = ['year'])

df =df[['location','year','total_cases','new_cases','total_deaths','new_deaths']]

## aggreate total_cases, new_cases, total_deaths, new_deaths from DataFrame.
## the agg() logic as same as parta1 agg()
df = df.groupby(['location','year'],as_index=False).agg({'total_cases':'max','new_cases':'sum','total_deaths':'max','new_deaths':'sum'})

## caculate fatality rate in the year 2020
df['case_fatality_rate'] = df['new_deaths']/df['new_cases']

## rearrange df columns
df = df[['location','year','case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]

## get command line arguments 
parser = argparse.ArgumentParser()
parser.add_argument("graph1")
parser.add_argument("graph2")
agrs = parser.parse_args()

## scatter plot grpah a
df.plot.scatter(x = 'new_cases',y = 'case_fatality_rate',grid = True, s = 5)
plt.title("scatter-a")
plt.savefig(agrs.graph1)

## scatter plot grpah b
df.plot.scatter(x = 'new_cases',y = 'case_fatality_rate',grid = True, s = 5,logx=True)
plt.title("scatter-b")
plt.xlabel("log_new_cases")
plt.savefig(agrs.graph2)