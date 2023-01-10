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
csvpath = os.path.join(now,'Resources','election_data.csv')

#------------------------------------------------------------------------------------

# Making the path a file
with open(csvpath) as csvfile:

     #csv reader specifies delimiter and variable that holds desired contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove the headers from the dataset 
    headers = next(csvreader)

#------------------------------------------------------------------------------------

    # create variables to separate the data (the only column that is important is 
    # the names column)

    # variable for the candidates

    candidates = []

    for row in csvreader:
        candidates.append(row[2])

#------------------------------------------------------------------------------------

    # total number of votes cast

    tot_votes = len(candidates)

#------------------------------------------------------------------------------------

    # Display Data

    # create a path to the analysis text file in the analysis folder

    path = os.path.join(now, 'analysis', 'analysis.txt')

#------------------------------------------------------------------------------------
            
    # percentage and number of votes each candidate won

    # use the counter function to get the number of unique occurances

    from collections import Counter

    new = Counter(candidates)

    
#------------------------------------------------------------------------------------

    # create the analysis txt file with all the outputted data
    # it is important to start the analysis file here for the 
    # for loop to add the data properly, otherwise the loop will
    # overwrite the file

    with open( path , 'w') as ana:
        print('Election Results', file=ana)
        print('-------------------------------------', file=ana)
        print(f'Total Votes:', tot_votes, file=ana)
        print('-------------------------------------', file=ana)

    # print to terminal
        print('Election Results')
        print('-------------------------------------')
        print(f'Total Votes:', tot_votes)
        print('-------------------------------------')
#------------------------------------------------------------------------------------
    # for loop to output the results for each candidate

        # most_common produces the most common element and their counts
        # from greatest to least
        new.most_common() 
        
        # value and count are variables that store the respective 
        # unique element and the number of occurances for the counter


        # built in property of most_common, the first value in the loop 
        # will be the highest occurance and thus the winner

       
        
        for value, count in new.most_common():
            
            # percentage of votes received
            per = (count/tot_votes)*100
            # candidates, percent of votes, and vote count in order from greatest
            # to least. 
            print(f"",value,':', per, '%', '(',count,')',file=ana)

            # print to terminal
            print(f"",value,':', per, '%', '(',count,')')

        print('-------------------------------------', file=ana)

        # print to terminal
        print('-------------------------------------')

#------------------------------------------------------------------------------------
        # winner with the most votes       
        # built in property of most_common, the first value  
        # will be the highest occurance and thus the winner
        print(f"Winner:" , new.most_common(1)[0][0], file=ana)
        print('-------------------------------------', file=ana)


        # print to terminal

        print(f"Winner:" , new.most_common(1)[0][0])
        print('-------------------------------------')


   





