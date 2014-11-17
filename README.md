#Data Analysis

This project contains some exercises in data analysis with python-pandas and some comparisons with raw python.

The **goal** is to learn and have some fun.

The files processed to obtain the data will not be published (are not mine to decide)

##Tasks

###First exercise: 
count the number of lines in Python for each file

Solution and discussion [here](http://nbviewer.ipython.org/github/leomrocha/data-analysis-exercises/blob/master/1st%20Exercise.ipynb)

###Second exercise:

Arrival airport is the column arr_port. It is the IATA code for the airport

1. Print the top 10 arrival airports in the standard output, including the number of passengers.
2. (E) Get the name of the city or airport corresponding to that airport

Solutions and discussion [here](http://nbviewer.ipython.org/github/leomrocha/data-analysis-exercises/blob/master/2nd%20Exercise.ipynb)

3. (E) Write a Web Service taht wraps the output of the exercise that returns the data in JSON format. The web service should accept a parameter n>0. For the top 10 airports, n is 10. For the X top airports, n is X.



###Third exercise:

1. Plot the monthly number of searches for flights arriving at Málaga, Madrid or Barcelona.

Solutions and discussion [here](http://nbviewer.ipython.org/github/leomrocha/data-analysis-exercises/blob/master/3rd%20Exercise.ipynb)

2. (E) For every search in the searches file, find out whether the search ended up in a booking or not. Write a file with the results.


###Bonus Exercise: Ranking Web Service

Wrap the output of the second exercise in a web service that returns the data in JSON format (instead of printing to the standard output). The web service should accept a parameter n>0. For the top 10 airports, n is 10. For the X top airports, n is X.

#### Notes

This exercise is solved in the files:

 * ranker.py : contains the ranking algorithm
 * ws_rank.py : contains the web service (depends on bottle.py)

#### Dependences

 * bottle.py
 * pandas

#### System requirements

The program load the complete dataset in memory for the table bookings.py. The system needs enough memory for pandas to be able to load it.

#### Launching

To launch the program: 
$ python  ws_rank.py 


#### Usage
The program returns a json object containing the airport and the number of passengers (pax).

Getting the n top arrival airports:

    localhost:8080/arrivals/first/100

Getting the n last arrival airports:
    
    localhost:8080/arrivals/last/100

##Possible problems

###Lacking familiarity with Pandas library
**Solutions:**

 * Study
 * Search documentation, forums, StackOverflow, and tutorials
 * Compare results with pure python for checking correctness and performance comparison

###Memory

**Solutions:**

 * Load file in chunks
 * Load only needed columns
 * Use file storage (PyTables)

##Plan (not strict, but as a guide)

1. Read documentation about pandas.
2. Do some testing on dummy data
3. Do a basic analysis of the data (format, separators, columns, number of rows)
4. Go to more complex tasks
5. Publish one result a day until finish
6. Packaging
7. Installation and usage documentation

##Conclussions

I had some fun and started learning a new library
###Lessons learned:

 * I started learning Python Pandas library
 * I had some fun
 * I underestimated the effort needed to learn to use the library
 * I found more problems than expected
 * Check, once and again formatting and separators in input files.
 * Warning with missing data





