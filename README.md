# python-challenge

In this challenge I used python to analyze csv files and produce analytical data. 

I used os.path.join to create the paths for the code to determine where the appropriate files were
At first it wasn't working, but I determined what .join did to the code (adds the elements to the end 
of the path). Therefore I needed to take the parent directory and add the elements to the end of it to 
form the entire path.

I found that the best way for me to get the desired values was to use append to create variables
with the desired vales in them, then to take sums or extract data. 

To export the data to a txt file I created a path to the text file and populated it to the text file
by adding file=ana (the name of the file variable)

For the PyPoll challenge I chose to use the built in function Counter to provide the desired values
I then used the properites of python (the order in which the code is run and the characteristics of 
the for loop) to produce the desired values and reduce the amount of code I had to write. 

I found the different properties of the Counter (most_common) and used them to make the process of 
getting the desired values easier. 
