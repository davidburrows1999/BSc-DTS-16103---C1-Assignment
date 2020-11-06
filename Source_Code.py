""" 

Software Fundamentals C1 Test 
David Burrows
Abortion Statistic Parse, Process and Plot

"""

#Importing the modules that are needed for the programme 
#Importing the pandas data science library that allows you to manipulate a dataframe
#Importing the matplotlib which allows you to plot data on python and can be integrated with Pandas 
#As pd just for ease rather than typing out pandas every time 
import pandas as pd
import matplotlib as plt
import numpy as np

#using pandas we set the max columns so that we can see the whole dataframe in the output console
pd.set_option('display.max_columns', 20)

#load in the data as a dataframe (using panadas.read function) which is the object that allows us to manipulate data
df = pd.read_csv(r"C:\Users\612811261\OneDrive - BT Plc\Documents\University\Ravensbourne\Year 1 Term 2\Software Fundementals\Abortion_rates.csv")

#Firstly take a look at the data set with sample and shape to understand what the data looks like 
#This will get two rows for an example 
print(df.sample(2))

#This tell us how many columns and rows we are working with  
print(df.shape)

#Then we print the column titles or headers so that we know what to use later on
print(df.columns)

#Now we have the data the first thing we want to do is get the total number of abortions for each year
#For this we will need to add up rows 4-10 and I would like to make it a new row at the bottom

#Create a variable totals and set that to the sum of the rows 2-8 containing the total number of abortions using .sum
totals = (df[2:9].sum())

#Use the df.append from the pandas library to add the information in the totals variable to a new row. The ignore_index is needed so that no new indexing is done
df = df.append(totals[1:],ignore_index=True)

#df.at is used to change the name of the new row to Total. This is done by specifying the exact location through the column name and the row 
df.at[9,"Age"]= "Total per Year"

#Secondly what we want to do is add the information in 2001-2009 for each age category and add that as a new column 
#Create a new column then use iloc to get the rows for the information that we want and sum the rows 
df["Total all Years"] = df.iloc[0:,0:].sum(axis=1)

#Using the mean function and iloc. to specify location to calculate the average number of abortions over the 9 year span
df["Average Over Years"] = df.iloc[0:,1:10].mean(axis=1)

#Using Pandas display format change the display format for the column created so that we only have 2 decimal points 
pd.options.display.float_format = "{:,.2f}".format

#Create a new row which details the average rate for abortions every hour over that year using iloc to get the specific rows 
df.loc[10] = (df.iloc[9,][1:10] / 365) / 24 
#Change the name so that the Age colomn is correct 
df.at[10,"Age"] = "Hourly Avg Rate"

#Sort by Avg Daily rate
#Create a new dataframe to store the sort which drops all the columns that we don't need (and contain text which produces an error)
Hourly_rate_sort = df.drop(["Age", "Total all Years", "Average Over Years"], axis=1)
#Sort the values by the 10 index, axis is set to one to denote that we are showing rows. Inplace will select the original object itself 
Hourly_rate_sort.sort_values(by =10, axis = 1, ascending=False, inplace=True)
print(Hourly_rate_sort)

#Percentage of Average over years...I.E. The percentage each age range has contributed on average
df["Percentage of Total"] = (df.loc[0:8]['Average Over Years']/df["Average Over Years"][9]) * 100
print(df)

#Plot a line graph that shows the total abortions per year for every year

#Firstly we need to take the original dataframe and drop the colomns and headings that we do not need 
Total_abortions_plot_df = df.drop(["Average Over Years","Percentage of Total","Total all Years"], axis=1).drop(df.index[0:9], axis=0).drop(df.index[10], axis=0)
#Now the data is transposed so that we can have two colomns with one representing the Age and the Total Per Year 
Total_abortions_plot_df = Total_abortions_plot_df.transpose()

#This leaves us with an index as a colomn header so we have to replace this with the titles that we want so we can plot
#take the first row for the header
new_header = Total_abortions_plot_df.iloc[0] 
#take all the data besides the header row
Total_abortions_plot_df = Total_abortions_plot_df[1:] 
 #set the header row as the new dataframe header
Total_abortions_plot_df.columns = new_header


print(Total_abortions_plot_df)
#Plot the Total Abortions per year with the kind as a bar graph using the plot function. 
Total_abortions_plot_df.plot(y=0, kind="bar")
ax = Total_abortions_plot_df.plot(y=0,kind="line")
#Plot a graph of the total abortion deaths per year vs the total

#load in the data as a dataframe (using panadas.read function) which is the object that allows us to manipulate data
Total_deaths_UK_df = pd.read_csv(r"C:\Users\612811261\OneDrive - BT Plc\Documents\University\Ravensbourne\Year 1 Term 2\Software Fundementals\Total_Deaths_England_and_Wales.csv")

#The total death data included some other unwanted data so using the iloc function we can get rid of this
Total_deaths_UK_df = Total_deaths_UK_df.iloc[0:10][:]
#Print check to see if the data was imported correctly and whether the iloc has worked
print(Total_deaths_UK_df)
#Issues can occur when the data is in the string format so using the df.astype function we change it to integer 
Total_deaths_UK_df = Total_deaths_UK_df.astype(int)
#Plot the data in a separate graph to see what it looks like by itself
Total_deaths_UK_df.plot(y="Deaths", x="Year", kind="line")


#Using the ax label we take the total abortions plot and the total deaths plot and we plot them together on the same chart 
# the ylim is also setting limits on the axis so that the data can be seen in an effective way
Total_vs_abortions_plot = Total_deaths_UK_df.plot(ax=ax, ylim = (150000,550000))
#In this case it also plotted a line on the axis for years. to get rid of this I just used the .remove function on the first line that we had plotted 
Total_vs_abortions_plot.lines[1].remove()


















