#Data Analysis

This project contains some exercises in data analysis with python-pandas and some comparisons with raw python.

The **goal** is to learn and have some fun.

The files processed to obtain the data will not be published (are not mine to decide)

##Tasks

###First exercise: 
count the number of lines in Python for each file


###Second exercise:

Arrival airport is the column arr_port. It is the IATA code for the airport

1. Print the top 10 arrival airports in the standard output, including the number of passengers.
2. (E) Get the name of the city or airport corresponding to that airport
3. (E) Write a Web Service taht wraps the output of the exercise that returns the data in JSON format. The web service should accept a parameter n>0. For the top 10 airports, n is 10. For the X top airports, n is X.

###Third exercise:

1. Plot the monthly number of searches for flights arriving at Málaga, Madrid or Barcelona.
2. (E) For every search in the searches file, find out whether the search ended up in a booking or not. Write a file with the results.

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

##Plan (not strict, but as a guide)

1. Read documentation about pandas.
2. Do some testing on dummy data
3. Do a basic analysis of the data (format, separators, columns, number of rows)
4. Go to more complex tasks
5. Try to publish one result a day until
6. Packaging
7. Installation and usage documentation


