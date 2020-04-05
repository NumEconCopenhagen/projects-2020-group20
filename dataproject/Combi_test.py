#####################################################################################################################
import pandas as pd
from datetime import datetime


# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject
#####################################################################################################################

# A. load data without unnecessary data
raw_input = pd.read_csv('PL_all_seasons.csv', \
usecols=['Date','HomeTeam','AwayTeam','FTR','B365H','B365D','B365A'])

# B. convert date from string to datetimes
raw_input['Date'] = pd.to_datetime(raw_input['Date'], dayfirst = True)

# append seasons
# Add a new column named 'season' 
Type_new = pd.Series([])

# running a for loop and asigning some values to series 
for i in range(len(raw_input)): 
    if raw_input["Date"][i] < datetime(2010, 8, 10): 
        Type_new[i]="09/10"
  
    elif raw_input["Date"][i] < datetime(2011, 8, 10): 
        Type_new[i]="10/11"
  
    elif raw_input["Date"][i] < datetime(2012, 8, 10):  
        Type_new[i]="11/12"
  
    elif raw_input["Date"][i] < datetime(2013, 8, 10):  
        Type_new[i]="12/13"
  
    elif raw_input["Date"][i] < datetime(2014, 8, 10):  
        Type_new[i]="13/14"
    
    elif raw_input["Date"][i] < datetime(2015, 8, 10):  
        Type_new[i]="14/15"
  
    elif raw_input["Date"][i] < datetime(2016, 8, 10):  
        Type_new[i]="15/16"

    elif raw_input["Date"][i] < datetime(2017, 8, 10):  
        Type_new[i]="16/17"
  
    elif raw_input["Date"][i] < datetime(2018, 8, 10):  
        Type_new[i]="17/18"
  
    elif raw_input["Date"][i] < datetime(2019, 8, 10):  
        Type_new[i]="18/19"

    else: 
        season[i]= raw_input["Date"][i] 
  
        
        # inserting new column with values of list made above         
raw_input.insert(2, "Season", Type_new) 
# raw_input.head(10)
#####################################################################################################################

# Combine total data frame

df = pd.DataFrame(raw_input)

# d. add boolean of result Home, Draw, Away and then print df

df['H_true'] = df['FTR'].str.count("H")
df['D_true'] = df['FTR'].str.count("D")
df['A_true'] = df['FTR'].str.count("A")
df.head(10)

# e. multiply bolean of Draw (D_true) with B365 odds of draw to get each games return for you

return_D = ( df.loc[:, 'D_true'] * df.loc[:, 'B365D'] )

print(return_D)

# f. sum these individual returns to get you full season return

sum_return_D = return_D.sum()
print(sum_return_D)

# count entries
No_of_matches = df.Date.count()
print(No_of_matches)

#g. find the net return by subtracting the DKK 1 * No of matches = DKK x you have betted during the season to find your gain/loss

net_return_D = sum_return_D - No_of_matches

print(net_return_D)

#g. find the return in percentage by dividing you gain with the DKK 1 * 380 games = DKK 380 you have betted during the season and subtract 1.

net_pct_returm_D = sum_return_D / No_of_matches - 1

print(net_pct_returm_D)

#####################################################################################################################

 Returns = {'Season':['09/10','10/11','11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19']}
 Return_df = pd.DataFrame(Returns, columns = ['Season'])
 Return_df
 Seasonal_return = []

 for x in df['Season']:
   if x == '09/10':
        return_D = ( df.loc[:, 'D_true'] * df.loc[:, 'B365D'] )
        sum_return_D = return_D.sum()
        No_of_matches = df.Date.count()
        net_return_D = sum_return_D - No_of_matches
         net_pct_returm_D = sum_return_D / No_of_matches - 1
     Seasonal_return.append(net_pct_returm_D)

    else 'Hello'

Return_df['Seasonal return'] = Seasonal_return
Return_df    


#####################################################################################################################

df['Return_D'] = df.D_true * df.B365D
df['Return_A'] = df.A_true * df.B365A
df['Return_H'] = df.H_true * df.B365H
df.head(10)

#####################################################################################################################
Season_group = df.groupby(['Season','FTR']).sum()
drop_these = ['B365H','B365D','B365A']
Season_group.drop(drop_these, axis=1, inplace=True)
Season_group