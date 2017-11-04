
# Heroes Of Pymoli Data Analysis

* OBSERVED TREND 1
    Most players are male

* OBSERVED TREND 2 
    Most players are between 20 and 24

* OBSERVED TREND 3
    In the larger dataset, all of the most popular items are less expensive than the average purchase price and all of the most profitable items are more expensive than the average purchase price


```python
# load dependencies
import pandas as pd
from collections import OrderedDict
```


```python
# save filepath to json file
json_file = 'C:/Users/Kali/Dropbox/documents/data science/Data Bootcamp/hw/HeroesOfPymoli/purchase_data.json'

# load json file
df = pd.read_json(json_file)

# rename columns to remove spaces
cols = df.columns
cols = cols.map(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)
df.columns = cols
```


```python
# create function to generate summary info
def game_summary(df):
    
    df_count = df.shape[0] # generate purchase count
    avg_price = round(df.Price.mean(),2) # calculate average purchase price
    avg_price_f = '${0}'.format(avg_price) # format
    tot_price = round(df.Price.sum(),2) # calculate total purchase value
    tot_price_f = '${0}'.format(tot_price) #format
    users = len(df['SN'].unique()) # count number of users
    # calculate normalized totals
    if users == 0:
        norm_f = '0'
    else:
        norm = round(tot_price/users,2)
        norm_f = '${0}'.format(norm)
    
    return([users, df_count, avg_price_f, tot_price_f, norm_f])
```

## Player Count


```python
# report player count
all_summary = game_summary(df)
pd.DataFrame({"Total Players": all_summary[0]}, index = [0])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)


```python
# count number of unique items
unique_items = len(df.Item_Name.unique())

# create ordered dict with relevant data
purchases = OrderedDict({"Number of Unique Items" : [unique_items],
                         "Average Price" : all_summary[2],
                         "Number of Purchases" : all_summary[1],
                         "Total Revenue" : all_summary[3]})

purchases_df = pd.DataFrame(purchases) # create pandas df

purchases_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics


```python
df_male = df.loc[df['Gender'] == 'Male',:] # create subset df

df_female = df.loc[df['Gender'] == 'Female',:] # create subset df

df_other = df.loc[df['Gender'] == 'Other / Non-Disclosed',:] # create subset df

# create a list with the summary data for each of the subset dfs
gen_lists = [game_summary(df_male), game_summary(df_female), game_summary(df_other)]

# store column names
labels = ['Total Count', 'Purchase Count', 'Average Purchase Price', 'Total Purchase Value', 'Normalized Totals']

gens = ['Male', 'Female', 'Other/Non-Disclosed'] # store index names

gen_df = pd.DataFrame(gen_lists, columns = labels, index = gens) # create pandas df

gen_df_users = pd.DataFrame(gen_df['Total Count']) # create subset df
       
# create percentage column by calculating from Total Count column
gen_df_users['Percentage of Players'] = round((gen_df_users['Total Count']/all_summary[0]) * 100, 2)

gen_df_users
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>81.15</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>17.45</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>8</td>
      <td>1.40</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Gender)


```python
gen_df.drop(['Total Count'], axis = 1) # create subset df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics


```python
one = df.loc[df['Age'] <= 10,:] # create subset df
two = df.loc[(df['Age'] > 10) & (df['Age'] <= 14), :] # create subset df
three = df.loc[(df['Age'] > 15) & (df['Age'] <= 19), :] # create subset df
four = df.loc[(df['Age'] > 20) & (df['Age'] <= 24), :] # create subset df
five = df.loc[(df['Age'] > 25) & (df['Age'] <= 29), :] # create subset df
six = df.loc[(df['Age'] > 30) & (df['Age'] <= 34), :] # create subset df
seven = df.loc[(df['Age'] > 35) & (df['Age'] <= 39), :] # create subset df
eight = df.loc[df['Age'] > 40,:] # create subset df

# create a list with the summary data for each of the subset dfs
age_lists = [game_summary(one), game_summary(two), game_summary(three),
             game_summary(four), game_summary(five), game_summary(six),
             game_summary(seven), game_summary(eight)]

# store column names
labels = ['Total Count', 'Purchase Count', 'Average Purchase Price', 'Total Purchase Value', 'Normalized Totals']

# store index names
ages = ['<10', '11-14', '15-19','20-24', '25-29', '30-34', '35-39', '40+']

age_df = pd.DataFrame(age_lists, columns = labels, index = ages) # create pandas df

age_df_users = pd.DataFrame(age_df['Total Count']) # create subset df
       
# create percentage column by calculating from Total Count column
age_df_users['Percentage of Players'] = round((age_df_users['Total Count']/all_summary[0]) * 100, 2)

age_df_users
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>22</td>
      <td>3.84</td>
    </tr>
    <tr>
      <th>11-14</th>
      <td>20</td>
      <td>3.49</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>66</td>
      <td>11.52</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>186</td>
      <td>32.46</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>39</td>
      <td>6.81</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>34</td>
      <td>5.93</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>17</td>
      <td>2.97</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>0.52</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)


```python
age_df.drop(['Total Count'], axis = 1) # create subset df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>11-14</th>
      <td>31</td>
      <td>$2.7</td>
      <td>$83.79</td>
      <td>$4.19</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>86</td>
      <td>$2.86</td>
      <td>$246.06</td>
      <td>$3.73</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>238</td>
      <td>$2.92</td>
      <td>$696.09</td>
      <td>$3.74</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>58</td>
      <td>$2.82</td>
      <td>$163.81</td>
      <td>$4.2</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>46</td>
      <td>$3.07</td>
      <td>$141.24</td>
      <td>$4.15</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>30</td>
      <td>$2.75</td>
      <td>$82.38</td>
      <td>$4.85</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
# Identify the the top 5 spenders in the game by total purchase value
group_df = df.groupby(['SN'])
top5_count = pd.Series(group_df['Price'].count(), name = 'Purchase Count')
top5_avg = pd.Series(round(group_df['Price'].mean(),2), name = 'Average Purchase Price')
top5_spent = pd.Series(group_df['Price'].sum(), name = 'Total Purchase Value')

top5 = pd.concat([top5_count, top5_avg, top5_spent], axis=1)
top5 = top5.sort_values(['Total Purchase Value'],ascending = False)
top5 = top5.head(5)
top5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Item


```python
# Identify the 5 most popular items by purchase count
item_df = df.groupby(['Item_ID', 'Item_Name', 'Price'])
item_count = pd.Series(item_df['Price'].count(), name = 'Purchase Count')
item_spent = pd.Series(item_df['Price'].sum(), name = 'Total Purchase Value')

item5 = pd.concat([item_count, item_spent], axis=1)
item_count5 =  item5.sort_values(['Purchase Count'],ascending = False)
item_count5 = item_count5.head(5)
item_count5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item_ID</th>
      <th>Item_Name</th>
      <th>Price</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>2.35</th>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <th>2.23</th>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <th>2.07</th>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <th>1.24</th>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <th>1.49</th>
      <td>9</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items


```python
# Identify the 5 most profitable items by total purchase value
item_total5 =  item5.sort_values(['Total Purchase Value'],ascending = False)
item_total5 = item_total5.head(5)
item_total5
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item_ID</th>
      <th>Item_Name</th>
      <th>Price</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <th>4.14</th>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <th>4.25</th>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <th>4.95</th>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <th>4.87</th>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <th>3.61</th>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


