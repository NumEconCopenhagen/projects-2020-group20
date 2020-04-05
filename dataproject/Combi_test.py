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

Return_data = {'Season':['09/10','10/11','11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19']}
Return_df = pd.DataFrame(Return_data, columns = ['Season'])
Return_df


for row in df['Season']:
    if row == '09/10':
        D_sum_return0910 = df.Return_D.sum()
        A_sum_return0910 = df.Return_A.sum()
        H_sum_return0910 = df.Return_H.sum()
    elif row == '10/11':
        D_sum_return1011 = df.Return_D.sum()
        A_sum_return1011 = df.Return_A.sum()
        H_sum_return1011 = df.Return_H.sum()
    elif row == '11/12':
        D_sum_return1112 = df.Return_D.sum()
        A_sum_return1112 = df.Return_A.sum()
        H_sum_return1112 = df.Return_H.sum()
    elif row == '12/13':
        D_sum_return1213 = df.Return_D.sum()
        A_sum_return1213 = df.Return_A.sum()
        H_sum_return1213 = df.Return_H.sum()
    elif row == '13/14':
        D_sum_return1314 = df.Return_D.sum()
        A_sum_return1314 = df.Return_A.sum()
        H_sum_return1314 = df.Return_H.sum()
    elif row == '14/15':
        D_sum_return1415 = df.Return_D.sum()
        A_sum_return1415 = df.Return_A.sum()
        H_sum_return1415 = df.Return_H.sum()
    elif row == '14/15':
        D_sum_return1415 = df.Return_D.sum()
        A_sum_return1415 = df.Return_A.sum()
        H_sum_return1415 = df.Return_H.sum()
    elif row == '15/16':
        D_sum_return1516 = df.Return_D.sum()
        A_sum_return1516 = df.Return_A.sum()
        H_sum_return1516 = df.Return_H.sum()
    elif row == '16/17':
        D_sum_return1617 = df.Return_D.sum()
        A_sum_return1617 = df.Return_A.sum()
        H_sum_return1617 = df.Return_H.sum()
    elif row == '17/18':
        D_sum_return1718 = df.Return_D.sum()
        A_sum_return1718 = df.Return_A.sum()
        H_sum_return1718 = df.Return_H.sum()
    elif row == '18/19':
        D_sum_return1819 = df.Return_D.sum()
        A_sum_return1819 = df.Return_A.sum()
        H_sum_return1819 = df.Return_H.sum()

Return_D_test = [D_sum_return0910,D_sum_return1011,D_sum_return1112,D_sum_return1213,D_sum_return1314,D_sum_return1415,D_sum_return1516,D_sum_return1617,D_sum_return1718,D_sum_return1819]
Return_A_test = [A_sum_return0910,A_sum_return1011,A_sum_return1112,A_sum_return1213,A_sum_return1314,A_sum_return1415,A_sum_return1516,A_sum_return1617,A_sum_return1718,A_sum_return1819]
Return_H_test = [H_sum_return0910,H_sum_return1011,H_sum_return1112,H_sum_return1213,H_sum_return1314,H_sum_return1415,H_sum_return1516,H_sum_return1617,H_sum_return1718,H_sum_return1819]


Return_df['Return_test_D'] = Return_D_test
Return_df['Return_test_A'] = Return_A_test
Return_df['Return_test_H'] = Return_H_test
Return_df


