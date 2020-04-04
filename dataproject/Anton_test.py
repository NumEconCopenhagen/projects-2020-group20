import pandas as pd


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject

# a. load
raw_input = pd.read_csv('PL_all_seasons.csv')
print(raw_input)