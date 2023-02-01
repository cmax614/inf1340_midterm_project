#!/usr/bin/env python
# coding: utf-8

# ### Teng-Chieh Chuang 1004744752
# ### Programming for Data Science INF1340H F 
# ### Professor Maher Elshakankiri
# ### Master of Information 
# ### Faculty of Information
# ### Universtiy of Toronto 
# 
# 

# In[1]:


#Midterm Project
#created Oct 31, 2022
#Last Modified Oct 31, 2022


# In[5]:


import csv
import numpy as np
import matplotlib.pyplot as plt


# In[119]:


'''
This program takes a csv file containing information of a company's monthly stock prices, 
and can perfrom the following tasks:

    1. Show descriptive Statistics of the stock
    2. Retrieve stock price on a specific date
    3. Visualize the monthly stock prices with a plot
'''
#Finds the peak price of the stock and its corresponding date
def find_high(date_to_price):
    max_price = 0
    for i in date_to_price:
        if float(date_to_price[i]) > max_price:
            max_price = float(date_to_price[i])
            max_date = i
        
    return max_date, max_price

#find the lowest price of the stock and its corresponding date
def find_low(date_to_price):
    min_price = None
    for i in date_to_price:
        if min_price == None:
            min_price = float(date_to_price[i])
            min_date = i
        elif float(date_to_price[i]) < min_price:
            min_price = float(date_to_price[i])
            min_date = i
    return min_date, min_price

#find the average of the price
def find_mean_price(date_to_price):
    prices = []
    for i in date_to_price:
        prices.append(float(date_to_price[i]))
        avg = sum(prices) / 12 #Calculating mean price
    return avg

#Given the user input date, find the stock price on that specific date
def find_price(date_to_price, date):
    for i in date_to_price:
        if i == date:
            return date_to_price[i]
    
#Input the csv file
firm = str(input("Enter company file name(e.g. MCD)"))
handle = open((firm + ".csv"), 'r')
csv_reader = csv.DictReader(handle)

date_to_price = {} #Dictionary that stores the date and prices of the stock
Prices = [] #List that stores all the stock prices
Dates = [] #Lists that stores all the dates

for next_row in csv_reader:
    Prices.append(float(next_row["Adj Close"])) #Adds price to the list
    Dates.append(next_row["Date"]) #Adds date to the list
    date_to_price[(next_row["Date"])] = next_row["Adj Close"] #mapping Date to the price
    
#Calling the functions for statistics
max_date = (find_high(date_to_price)[0])
max_price = (find_high(date_to_price)[1])
min_date = (find_low(date_to_price)[0])
min_price = (find_low(date_to_price)[1])
mean_price = find_mean_price(date_to_price)

#calculation using numpy
prices = np.array(Prices)
price_sd = prices.std()
price_var = prices.var()
price_range = prices.max() - prices.min()

#Constructing the program with a while loop
while True:
    print("Menu: ")
    print("P = show descriptive statistics")
    print("V = Visualize monthly stock prices")
    print("D = Fetch price on given date")
    print("Q = Quit application")
    user_input = input("What do you want to do?[P,V,D,Q]")
    if user_input == "P":
        print("Over the past year, the stock price reached its peak on " + str(max_date) + " at$ " + str(max_price))
        print("Over the past year, the stock price was the lowest on " + str(min_date) + " at$ " + str(min_price))
        print("The range of the stock price was " + str(price_range))
        print("The average stock price over the last year was $" + str(mean_price))
        print("This stock has a standard deviation of " + str(price_sd) + " and variance of " + str(price_var))
    if user_input == "V":
        x = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
        y = Prices
        #Constructing the plot
        fig,ax = plt.subplots()
        ax.plot(x,y)
        ax.set_xlabel(Dates)
        ax.set_title("Monthly stock price")
        plt.show()
    if user_input == "D":
        date = input("Which date?(e.g. 2022-06-01)")
        print("The stock price on " + date + " is $" + find_price(date_to_price, date))
    if user_input == "Q":#Exit Program
        break
        


# In[72]:


numbers = np.array([1,4,9,16,25,36])
numbers2 = np.arange(1,7)*10
numbers3 = numbers2.reshape(2,3)
numbers4 = np.array([2,4,6])
numbers4.shape

