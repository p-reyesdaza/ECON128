
# coding: utf-8

# In[3]:


#Paula Reyes Daza Assignment 1

import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


df = pd.read_csv('bank-data.csv', sep=',', error_bad_lines=False)

print len(df)    # print number of rows
print list(df)   # print 1st header

df.head(1)


# 
# 
# (1) Explore the general characteristics of the data as a whole: examine the means, standard de-
# viations, and other statistics associated with the numerical attributes; show the distributions
# of values associated with categorical attributes; etc.

# In[56]:


#Analysis of 'Age' Data
print "~Age~"

print "Min: " , min(df['age'])
print "Max: " , max(df['age'])
print "Std: " , df['age'].std()
print "Avg: " , df['age'].mean()
print "Median:",df['age'].median()


# The average age is 42, but the standard devation indicates that there are a wide range of ages (18-67 year olds)

# In[133]:


#Analysis of 'Sex' Data
print '~Sex~'

sex_groupby = df.groupby('sex')

for key, value in sex_groupby:
    print  key, ":", len(value)


# There is an even number of males and females in the data set

# In[53]:


#Analysis of 'Region' Data
print '~Region~'

region_groupby = df.groupby('region')

for key, value in region_groupby:
    print key, ":", len(value)
    


# The people in this data set live in different area, with the least people living in suburban areas and the most living in inner city areas

# In[7]:


#Analysis of 'Income' Data
print '~Income~'

print "Min: " , min(df['income'])
print "Max: " , max(df['income'])
print "Std: " , df['income'].std()
print "Avg: " , df['income'].mean()
print "Median:",df['income'].median()


# The average income is about 27524, but there is a wide range of data which differs by a whole order of magnitude, since incomes go from 5014 to 63130

# In[26]:


#Analysis of 'Married Status' Data
print '~Married Status~'

married_groupby = df.groupby('married')

for key, value in married_groupby:
    print key, ":", len(value)


# most people in the data set are married

# In[12]:


#Analysis of 'Children' Data
print '~# of Children~'

print "Min: " , min(df['children'])
print "Max: " , max(df['children'])
print "Std: " , df['children'].std()
print "Avg: " , df['children'].mean()
print "Median:",df['children'].median()


# There are childless people, and people with 1, 2, or 3 kids. But it seems that most people in the data set have, on average, 1 child.

# In[50]:


#Analysis of 'Car' Data
print '~Car~'

car_groupby = df.groupby('car')


for key, value in car_groupby:
    print  key, ":", len(value)


# About half of the people have cars and the other half dont; there are only 8 more people without cars than with cars 

# In[22]:


#Analysis of 'Saving Account' Data
print '~Savings Account~'

savings_groupby = df.groupby('save_act')

for key, value in savings_groupby:
    print key, ":", len(value)


# More than half of the people in the data set have a savings account

# In[69]:


#Analysis of 'Current Account' Data
print '~Current Account~'

current_act_groupby = df.groupby('current_act')

for key, value in current_act_groupby:
    print key, ":", len(value)


# More than half of the people in the data set have a current (credit?) account. More people answered yes to having a current account than a savings account.

# In[24]:


#Analysis of 'Mortgage' Data
print '~Mortgage~'

mortgage_groupby = df.groupby('mortgage')

for key, value in mortgage_groupby:
    print key, ":", len(value)


# less than half of the people in the data set answered yes to having a mortgage 

# In[25]:


#Analysis of 'PEP' Data
print '~Personal Equity Plan~'

pep_groupby = df.groupby('pep')

for key, value in pep_groupby:
    print key, ":", len(value)
    


# Roughly half of the people in the data set have a PEP and the other half don't. More people don't have one.

# (2) Compare and constrast customers who do and don't buy PEP:

# In[144]:


pep_groupby = df.groupby('pep')

pep_age = pd.crosstab(df.age, df.pep)
print pep_age



# Seems like PEP-buyers are older than non-PEP buyers

# In[34]:


pep_sex =pd.crosstab(df.pep, df.sex)
print pep_sex
pep_sex.plot.bar()


# More men than women have PEPs

# In[35]:


pep_region =pd.crosstab(df.pep, df.region)
print pep_region

pep_region.plot.bar()


# Relatively, the number of people who live in each kind of region is still similar regardless of whether they do or dont buy PEP. The most people live in inner city and the least live in suburban regions for both subset of customers. However, in the suburban regions you can find more of the customers who buy PEPs, but in inner city and town regions you would find more of the costumers who don't buy PEPs

# In[141]:


pep_income = pd.crosstab(df.income, df.pep)
print pep_income


# Seems like PEP buyers are people who earn higher income than non-PEP buyers

# In[145]:


pep_married = pd.crosstab(df.pep, df.married)
print pep_married

pep_married.plot.bar()


# The married customers tend to not buy PEPs, since more of the married customers are in the no-PEP group. 

# In[42]:


pep_children = pd.crosstab(df.pep, df.children)
print pep_children

pep_children.plot.bar()


# In this data set, few of the people who buy PEPs have 3 children and many of the people who don't buy PEPs are childless. Only 25 of those don't buy PEPs have 1 child, while 110 of those who do buy PEPs have 1 child (1 = the most average number of children in the data set) so those who buy PEPs are more liekly to have the average number of children

# In[43]:


pep_car = pd.crosstab(df.pep, df.car)
print pep_car

pep_car.plot.bar()


# PEP vs no PEP groups dont seem to be signficantly different in their split between owning a car or not owning one

# In[44]:


pep_save_act = pd.crosstab(df.pep, df.save_act)
print pep_save_act

pep_save_act.plot.bar()


# Both PEP buyers and non buyers are more likely to have a savings account than to not have one. Doesnt seem like a sigificant difference, although more of the savings account holders are non-PEP buyers.

# In[45]:


pep_current = pd.crosstab(df.pep, df.current_act)
print pep_current

pep_current.plot.bar()


# Again, both PEP buyers and non buyers are more likely to have a current(credit?) account than to not have one. Doesnt seem like a sigificant difference, although more of the current account holders are non-PEP buyers.

# In[47]:


pep_mortgage =pd.crosstab(df.pep, df.mortgage)
print pep_mortgage

pep_mortgage.plot.bar()


# Both PEP buyers and non buyers are more likely to NOT have a mortgage. Doesnt seem like a sigificant difference, although more of those who do have a mortgage are non-PEP buyers.

# Overal thoughts on PEP vs. non-PEP customers:

# PEP buying versus non PEP buying customers are only somewhat differnet. They live in similar regions, proportionally. More of the saving account and credit account are non-PEP buyers, and less the mortgage buyers are part of the non-PEP buyers. Importantly, most of the married people and the childless people are not PEP buyers. Finally, PEP buyers seem to be older and to earn higher income than those who are in the non-PEP group.

# (3) Discretize the age attribute into 3 categories (corresponding to young, mid-age, and old)

# In[146]:


# 3 categories:
#Young: 0-30
#Mid-age: 31-60
#Old: 60+


age_discretize = df.groupby('age')


lst_one =[]
lst_two =[]
lst_three =[]

for key, value in age_discretize: 
    if key < 31:
        lst_one.append(len(value))
    elif 31 < key < 61:
        lst_two.append(len(value))
    elif 61 < key:
        lst_three.append(len(value))
        
    

one = sum(lst_one)
print "under 30 (young): ",one, "people"

two = sum(lst_two)
print "30 to 60 (mid-age): ", two, "people"


three = sum(lst_three)
print "60+ (old) : ", three, "people"





# (4) Using Matplotlib library and/or plotting capabilities of Pandas, create a scatter plot of the
# Income attribute relative to Age.

# In[134]:


from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

fig=plt.figure()
plt.scatter(df.income, df.age)
axis = fig.gca()
axis.set_title('Income vs Age')
axis.set_xlabel('Income')
axis.set_ylabel('Age')
fig.canvas.draw()

print "yes, these variables seem to be positively correlated"


# (5) Create histograms for Income (using 9 bins) and Age (using 15 bins)

# In[147]:


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

# remove NAN from array
x = df['income'][~np.isnan(df['income'])]
#isnan = for any value that is not a number i want to drop it

# plot histogram 
n, bins, patches = plt.hist(x, 9, normed=1, facecolor='green')
plt.title('Income Analysis')
plt.ylabel('Frequency')
plt.xlabel('Income')
plt.show()



import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

# remove NAN from array
x = df['age'][~np.isnan(df['age'])]
#isnan = for any value that is not a number i want to drop it

# plot histogram 
n, bins, patches = plt.hist(x, 15, normed=1, facecolor='purple')
plt.title('Age Analysis')
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.show()

