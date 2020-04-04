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
raw_input.head(5)

# convert date from string to datetimes
raw_input['Date'] = pd.to_datetime(raw_input['Date'])
print(raw_input)


# b. Summary statistics
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
print(raw_input)

# append seasons
# Add a new column named 'season' 
Type_new = pd.Series([])

# running a for loop and asigning some values to series 
for i in range(len(raw_input)): 
    if raw_input["Date"][i] < datetime(2010, 8, 15): 
        Type_new[i]="09/10"
  
    elif raw_input["Date"][i] < datetime(2011, 8,15): 
        Type_new[i]="09/10"
  
    elif raw_input["Date"][i] < datetime(2012, 8,15): 
        Type_new[i]="10/11"
  
    elif raw_input["Date"][i] < datetime(2011, 8,15): 
        Type_new[i]="11/12"
  
    elif raw_input["Date"][i] < datetime(2012, 8,15): 
        Type_new[i]="12/13"

    else: 
        season[i]= raw_input["Date"][i] 
  
        
        # inserting new column with values of list made above         
raw_input.insert(2, "Season", Type_new) 
  
# list output 
raw_input.head(0) 
print(raw_input)