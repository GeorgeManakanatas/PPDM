# PPDM
# Privacy Protecting Data Mining tool

#Description: 	
This is a program based on code that I used for my master's thesis in the Hellenic Open University.
As it stands now it will read data from a csv file, encrypt the attributes we want with native python encryption,
then use a simple k-anonymity method on the attributes we select (they must be different from those we encrypt)
then run an apriori algorithm on the resulting new data and return the results in a file.
		
#Goal:		
My goal is to eventually provide a free and open tool that can be used to demonstrate and test multiple simple k-anonymity and data mining techniques. 
As well as to be useful for comparison of different combinations of anonymity – encryption and data mining methods.
At this time I am working on a GUI so that changes in the attribute selection and other values can be made in a user friendly environment.
Also the long term goal is to add as many encryption, anonymity and data mining methods as possible.

#Files: 		
The files are divided into folders according to their function: Anonym methods contains files that are used for various k-anonymity methods.
For the time being it contains only Anonymise_simple and Kanon_file that we use for our simple method (may be merged into one file in future versions)
GUI contains the interface files and is still a work in progress
Data mining is used to store the data mining methods, as of now it contains an Apriori method that was uploaded to github under the MIT License
by the user asaini (abhinav saini) on the 7th of August 2013 modified to get data from main.

#Usage:		
For the time being the program can be executed by running the main.py file in python 2.7.
The file containing the data needs to be in the folder.
The parameters can only be changed from inside the code until the GUI is finished. 
The defaults are level of anonymity=3, attributes we want to anonymise = 1rst 2nd and 4th (0,1,3), attributes we want to encrypt= 3rd (2)
the minimum level of supprot = 0.3 and minimum level of confidence = 0.9 
These are applied to the included datafile that is census data from the census bureau database processed by the University of California Irvine.
The datafile source is the machine learning repository: https://archive.ics.uci.edu/ml/datasets/Adult	
	
#License:
MIT-License
