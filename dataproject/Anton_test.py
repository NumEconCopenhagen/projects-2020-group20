import pandas as pd


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject

# a. load data w/o unnecessary data
raw_input = pd.read_csv('PL_all_seasons.csv', \
usecols=['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A'])
raw_input.head(10)

