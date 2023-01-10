# This allows me to use files across operating systems 
import os

#------------------------------------------------------------------------------------

# Importing the budget data by creating a path to read csv file
import csv

#------------------------------------------------------------------------------------

## Create a variable with the csv path

# get the path to the current directory
now = os.getcwd()

# concatenate rest of path to budget data to create a full path
csvpath = os.path.join(now,'Resources','budget_data.csv')

#------------------------------------------------------------------------------------

# Making the path a file
with open(csvpath) as csvfile:

     #csv reader specifies delimiter and variable that holds desired contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove the headers from the dataset 
    headers = next(csvreader)

#------------------------------------------------------------------------------------
    
    # create a new variable with only the numerical values 

    # variable to store the values
    prof_loss = []

    # variable to store all of the months to index the greatest increase and decrease
    months = []

    # creating a list of the values using append 
    for row in csvreader:
        prof_loss.append(int(row[1]))
        months.append(row[0])

#------------------------------------------------------------------------------------

    # getting the total months
    tot_months = len(prof_loss)

#------------------------------------------------------------------------------------

    # getting the net total
    net_tot = sum(prof_loss)

#------------------------------------------------------------------------------------    

    # getting the average change
    
    # counter to collect the change values
    x = 1

    # variable to collect the change values
    difference = []


    for row in prof_loss:
        # if statement to ensure x doesn't exceed the range
        if x < tot_months:
            #calculating the change over the period
            diff = prof_loss[x] - row
            x = x + 1
            difference.append(diff)

    # importing the mean function to take the average
    from statistics import mean  

    ave_change = mean(difference)

#------------------------------------------------------------------------------------

    # finding the greatest increase

    great_incr = max(difference)

    # get the index to use on the month variable to get the month that value occured
    i = difference.index(great_incr)

#------------------------------------------------------------------------------------

    # finding the greatest decrease

    great_decr = min(difference)
    d = difference.index(great_decr)

#------------------------------------------------------------------------------------

    # Display Data

    # create a path to the analysis text file in the analysis folder

    path = os.path.join(now, 'analysis', 'analysis.txt')

    # create the analysis txt file with all the outputted data

    with open( path , 'w') as ana:

        print("Financial Analysis", file=ana )
        print("------------------------------------", file=ana)
        print(f"Total Months:" , tot_months, file=ana)
        print(f"Total: $" , net_tot, file=ana)
        print(f"Average Change: $" , ave_change, file=ana)
        # the index yields the row above the greatest increase because of the
        # calculation on line 70. Use i + 1 to adjust 
        print(f"Greatest Increase in Profits:" , months[i+1] ,"($",great_incr,")",file=ana)
        print(f"Greatest Decrease in Profits:" , months[d+1] ,"($",great_decr,")",file=ana)
  
    # print to terminal

        print("Financial Analysis" )
        print("------------------------------------")
        print(f"Total Months:" , tot_months)
        print(f"Total: $" , net_tot)
        print(f"Average Change: $" , ave_change)
        # the index yields the row above the greatest increase because of the
        # calculation on line 70. Use i + 1 to adjust 
        print(f"Greatest Increase in Profits:" , months[i+1] ,"($",great_incr,")")
        print(f"Greatest Decrease in Profits:" , months[d+1] ,"($",great_decr,")")