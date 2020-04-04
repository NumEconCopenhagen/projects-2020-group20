import pandas as pd


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject

# a. load data w/o unnecessary data
raw_input = pd.read_csv('PL_all_seasons.csv', \
usecols=['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A'])
raw_input.head(20)

# b. Summary statistics
raw_input.describe()

# draw dataframe
X_draw = pd.DataFrame(raw_input)
draws = X_draw.loc[X_draw['FTR']=='D',['B365H','B365D','B365A']]
print(draws)

# home dataframe
X_home = pd.DataFrame(raw_input)
home = X_home.loc[X_home['FTR']=='H',['B365H','B365D','B365A']]
print(home)

# away dataframe
X_away = pd.DataFrame(raw_input)
away = X_away.loc[X_away['FTR']=='A',['B365H','B365D','B365A']]
print(away)

# append seasons
df_w_seasons = pd.DataFrame(raw_input)
season = []
for row in df_w_seasons['Date']: 
    if row > '14/08/09':
        season.append('09/10')
    elif row > '13/08/10':
        season.append('10/11')
    elif row > '12/08/11':
        season.append('11/12')
    elif row > '17/08/12':
        season.append('12/13')
    elif row > '16/08/13':
        season.append('13/14')
    elif row > '15/08/14':
        season.append('14/15')
    elif row > '07/08/15':
        season.append('15/16')
    elif row > '12/08/16':
        season.append('16/17')
    elif row > '10/08/17':
        season.append('17/18')
    elif row > '09/08/18':
        season.append('18/19')
    else:
        season.append('lort')

df_w_seasons['Season'] = season
df_w_seasons
