import pandas as pd
from datetime import datetime


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject

# a. load data w/o unnecessary data
raw_input = pd.read_csv('PL_all_seasons.csv', \
usecols=['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A'])
raw_input.head(20)

# b. convert date from string to datetimes
raw_input['Date'] = pd.to_datetime(raw_input['Date'])
print(raw_input)

# c. Summary statistics
raw_input.describe()

# draw dataframe
X_draw = pd.DataFrame(raw_input)
draws = X_draw.loc[X_draw['FTR']=='D',['B365D']]
print(draws)

# home dataframe
X_home = pd.DataFrame(raw_input)
home = X_home.loc[X_home['FTR']=='H',['B365H']]
print(home)

# away dataframe
X_away = pd.DataFrame(raw_input)
away = X_away.loc[X_away['FTR']=='A',['B365A']]
print(away)

# append seasons
df_w_seasons = pd.DataFrame(raw_input)
season = []
for row in df_w_seasons['Date']: 
    if row > datetime(2009, 8, 15):
        season.append('09/10')
    elif row > datetime(2010, 8, 13):
        season.append('10/11')
    elif row > datetime(2011, 8, 12):
        season.append('11/12')
    elif row > datetime(2012, 8, 17):
        season.append('12/13')
    elif row > datetime(2013, 8, 16):
        season.append('13/14')
    elif row > datetime(2014, 8, 15):
        season.append('14/15')
    elif row > datetime(2015, 8, 15):
        season.append('15/16')
    elif row > datetime(2016, 8, 12):
        season.append('16/17')
    elif row > datetime(2017, 8, 10):
        season.append('17/18')
    elif row > datetime(2018, 8, 9)':
        season.append('18/19')
    else:
        season.append('lort')

df_w_seasons['Season'] = season
df_w_seasons
