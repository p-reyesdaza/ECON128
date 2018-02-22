
# coding: utf-8

# # HW 2 - PART 1

# In[232]:


#Paula Reyes Daza
import pandas
import sqlite3


# In[233]:


sqlite_file = 'flights.db'
conn = sqlite3.connect(sqlite_file)  # connect to database and ingest the tables 


# 1. Find/Print the number of airlines in the 'United States'

# In[234]:


query = "SELECT country, count() FROM airlines WHERE country like 'United States';"

quantity_airlines= pandas.read_sql(query, conn)
quantity_airlines.head()


#     2. Find/Print the routes that have one or more stops

# In[235]:


query2 = "SELECT airline, source, dest, stops FROM routes WHERE stops >=1;"

route_stops= pandas.read_sql(query2, conn)
print route_stops


#     3. Find/print the latitude and longitude of all airlines in the 'United States'

# In[236]:


query3 = "SELECT * FROM airlines WHERE country like 'United States';"

outcomes1= pandas.read_sql(query3, conn)
outcomes1.head()


# In[237]:


query4 = "SELECT * FROM airports;"

outcomes2 = pandas.read_sql(query4, conn)
outcomes2.head()


# In[238]:


#Join Airlines and Airports and print all the longitudes and latitudes of all the airlines in the US

query5 = "SELECT latitude, longitude, airlines.country, airlines.name         FROM airports JOIN airlines          ON airports.icao=airlines.icao         WHERE airlines.country like 'United States';"


question3 = pandas.read_sql(query5, conn)
print question3



#     4. Print/Find average latitude for each country listed in the airports table

# In[239]:


query6 = "SELECT country, AVG(latitude) as Average_Latitude FROM airports GROUP BY country;"

question4 = pandas.read_sql(query6, conn)
question4.head()


#     5. Insert new entry into the table routes

# In[249]:


#insert another entry, specifying everything (made up entries) except the index number
query7 = "INSERT INTO routes (airline, airline_id, source, source_id, dest, dest_id, codeshare, stops, equipment) VALUES ('3X', 960, 'JFK', 2300, 'LAX', 4500, 'Y', 3, 'CR2');"

cursor = conn.cursor()
cursor.execute(query7)
conn.commit()


# In[251]:


#Just checking that the entry is in there
query_check = "SELECT * FROM routes WHERE stops >2;"

checking= pandas.read_sql(query_check, conn)
print checking


#     6. Find/print all the routes originating from airports in the city of LA

# In[240]:


query8 = "SELECT source, dest         FROM airports as A JOIN routes as R          ON A.code=R.source         WHERE city like 'Los Angeles';"


question6 = pandas.read_sql(query8, conn)
print question6


#     
#        Extra credit Attempt: Plot airport latitude/longitude on a US Map

# In[283]:


bonus_query = "SELECT name, longitude, latitude FROM airports;"

extra_credit = pandas.read_sql(bonus_query, conn)

df = pandas.DataFrame(extra_credit)
print df


# In[ ]:


import matplotlib.pyplot as plt
df.plot(kind="scatter", x = 'longitude', y = 'latitude', alpha=0.4)
df.plt.show()

