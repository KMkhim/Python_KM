#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation with pandas
# Run the hidden code cell below to import the data used in this course.

# In[3]:


# Import the course packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the four datasets
avocado = pd.read_csv("datasets/avocado.csv")
homelessness = pd.read_csv("datasets/homelessness.csv")
temperatures = pd.read_csv("datasets/temperatures.csv")
sales = pd.read_csv("datasets/walmart.csv")


# ## Transforming DataFrames
# 
# Learn how to inspect DataFrames and perform fundamental manipulations, including sorting rows, subsetting, and adding new columns.

# <h3> Inspecting a DataFrame </h3>

# .head() returns the first few rows (the “head” of the DataFrame).

# In[4]:


print(homelessness.head())


# .info() shows information on each of the columns, such as the data type and number of missing values.

# In[5]:


print(homelessness.info())


# .shape returns the number of rows and columns of the DataFrame.

# In[6]:


print(homelessness.shape)


# .describe() calculates a few summary statistics for each column.

# In[7]:


print(homelessness.describe())


# <h3>Parts of a DataFrame</h3>

# .values  : A two-dimensional NumPy array of values.

# In[8]:


print(homelessness.values)


# .columns: An index of columns: the column names.

# In[9]:


print(homelessness.columns)


# .index: An index for the rows: either row numbers or row names.

# In[10]:


homelessness.index


# <h3>Sorting rows</h3>

# In[11]:


homelessness_ind = homelessness.sort_values("individuals")
homelessness_ind


# In[12]:


homelessness_ind = homelessness.sort_values("individuals" , ascending = False)
homelessness_ind


# <h4>multiple column </h4>
# <p>df.sort_values(["breed", "weight_kg"]) </p>

# <h3>Subsetting columns</h3>

# In[13]:


individuals = homelessness["individuals"]
individuals


# In[14]:


state_fam = homelessness[["state","family_members"]]
state_fam


# <h3>Subsetting rows</h3>

# In[15]:


ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
ind_gt_10k


# In[16]:


# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) &(homelessness["region"] == "Pacific")]

fam_lt_1k_pac


# <h3>Subsetting rows by categorical variables</h3>

# In[17]:


south_mid_atlantic = homelessness[homelessness['region'].isin(['South Atlantic','Mid-Atlantic'])]

south_mid_atlantic


# <h3>Add Column</h3>

# In[18]:


# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"]/homelessness["total"] 

# See the result
homelessness.head()


# # Chapter 2
# ## Aggregating DataFrames
# In this chapter, you’ll calculate summary statistics on DataFrame columns, and master grouped summary statistics and pivot tables.

# In[19]:


sales.head()


# <h3> Mean and median </h3>

# In[20]:


# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())


# <h3>Min and Max</h3>

# In[21]:


# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())


# <h3> Efficient summaries </h3>

# df['column'].agg(function)

# In[22]:


# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# In[23]:


#Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))


# In[24]:


print(sales[["temperature_c","fuel_price_usd_per_l" , "unemployment"]].agg(iqr))


# In[25]:


print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr , np.median]))


# <h3>Cumulative statistics</h3>

# In[26]:


sales_1_1 = sales.sort_values(["date" , "weekly_sales"])
sales_1_1 = sales[(sales["weekly_sales"] > 20000) & (sales["weekly_sales"] < 60000)]


# In[27]:


# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales["weekly_sales"].cummax()

# See the columns you calculated
sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]]


# <h3>Dropping duplicates</h3>

# In[28]:


store_types = sales.drop_duplicates(subset =["store","type"])
store_types


# In[29]:


store_depts = sales.drop_duplicates(subset=["store" , "department"])


# In[30]:


# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset = ['date'])
holiday_dates


# <h3>Counting categorical variables</h3>

# In[31]:


print(store_types['type'])


# In[32]:


# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)


# In[33]:


# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize = True)
print(store_props)


# In[34]:


# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort = True)
print(dept_counts_sorted)


# In[35]:


dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)


# <h3> Calculations with .groupby() </h3>

# In[36]:


# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type =  sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)


# In[37]:


# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([min,max,np.mean,np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


# <h3>Pivoting on one variable </h3>

# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.

# In[38]:


mean_sales_by_type = sales.pivot_table(values = "weekly_sales" , index = "type")
mean_sales_by_type


# Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type
# 

# In[39]:


mean_med_sales_by_type = sales.pivot_table(values = "weekly_sales" , index = "type" , aggfunc = [np.mean , np.median])
print(mean_med_sales_by_type)


# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.

# In[40]:


mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")
print(mean_sales_by_type_holiday)


# Print mean weekly_sales by department and type; fill missing values with 0
# 

# In[41]:


sales.pivot_table(values = "weekly_sales",index ='department' , columns ='type' ,fill_value=0)


# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols

# In[42]:


print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value = 0 ,margins = True))


# # Chapter 3
# ## Slicing and Indexing DataFrames
# 
#  Learn how they can be combined with slicing for powerful DataFrame subsetting.

# <h3>Setting and removing indexes</h3>

# In[73]:


temperatures


# In[44]:


temperatures_ind = temperatures.set_index("city")
temperatures_ind


# In[45]:


temperatures_ind.reset_index()


# In[46]:


temperatures_ind.reset_index(drop = True)


# <h3> Subsetting with .loc[] </h3>

# In[47]:


# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])


# In[48]:


print(temperatures_ind.loc[cities])


# <h3>Setting multi-level indexes</h3>

# In[49]:


# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


# <h3>Sorting by index values</h3>

# In[50]:


temperatures_ind.sort_index()


# In[51]:


temperatures_ind.sort_index(level = "city")


# In[52]:


temperatures_ind.sort_index(level = ["country","city"],ascending = [True , False])


# <h3>Slicing index values</h3>

# In[54]:


temperatures_srt = temperatures_ind.sort_index()
temperatures_srt


# In[55]:


# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])


# In[56]:


# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])


# In[57]:


# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan" , "Lahore"):("Russia" , "Moscow")])


# In[58]:


# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])


# In[60]:


# Subset in both directions at once
print(temperatures_srt.loc[("India","Hyderabad") : ("Iraq","Baghdad"),"date":"avg_temp_c"])


# <h3> Slicing time series </h3>

# In[61]:


# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)


# In[62]:


# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()


# In[63]:


# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])


# In[65]:


# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])


# <h3> Subsetting by row/column number </h3>

# In[66]:


# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[:23,:1])


# In[67]:


# Use slicing to get the first 5 rows
print(temperatures.iloc[:6])


# In[68]:


# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:5])


# In[69]:


# Use slicing in both directions at once
print(temperatures.iloc[:6 , 2:5])


# <h3>Pivot temperature by city and year</h3>

# In[78]:


temperatures.info()

# # Add a year column to temperatures
# temperatures["year"] = temperatures["date"].dt.year

# # Pivot avg_temp_c by country and city vs year
# temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index =["country" , "city"] ,columns = "year" )

# # See the result
# print(temp_by_country_city_vs_year)

