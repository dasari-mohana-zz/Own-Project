# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:33:46 2020

@author: MOHANA D
"""

# importing the library
from covid import Covid

# initializing
covid = Covid()
# printing data for the world
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())

# Gettingthe data according to country name
# Here data will be stored as a dictionary
cases = covid.get_status_by_country_name("india") # can use any other country to get data

# printing country's data using for loop
for x in cases:
    print(x, ":", cases[x])