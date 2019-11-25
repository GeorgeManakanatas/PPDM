<img align="right" src="./GUI/images/NEW_LAND_GRAPH1.png">
<!-- <img align="center" src="./GUI/images/PPDM_landing_large_graphic.png"> -->

# PPDM
Privacy Protecting Data Mining tool

##Description: 	
This is a program based on code that I used for my master's thesis in the Hellenic Open University.
As it stands now it will read data from a csv file, encrypt the attributes we want with native python encryption,
then use a simple k-anonymity method on the attributes we select (they must be different from those we encrypt)
then run an apriori algorithm on the resulting new data and return the results in a file.

##Goal:		
My goal is to eventually provide a free and open tool that can be used to demonstrate and test multiple simple k-anonymity and data mining techniques.
As well as to be useful for comparison of different combinations of anonymity – encryption and data mining methods.
At this time I am working on a GUI so that changes in the attribute selection and other values can be made in a user friendly environment.
Also the long term goal is to add as many encryption, anonymity and data mining methods as possible.

## File structure

The file structure of the project in detail.

The root folder contains fundamental files and the node_modules filder.
All front_end components are in the front end folder and all back end components
in the back_end folder. The goal for now is to use npm for moth the front
and back end in order to keep a common modules folder as well as to keep
common configuration folder.

```
root
-- main.py							# Starts the application
-- defaultConfig.json		# Baseline configuration (more as a set of default values)
--
-- Readme.md         		# The project readme file
---- GUI/        									# Contains all the tkinter gui code
			+-- GUI_call_from_main.py		# The interface called from main to configure the run
			+-- license.py							# The license agreement
---- functions/      									# Contains generic functions that fit not other folder
			+-- getDataInfo.py							# Misnamed file that reads the data from the csv
			+-- encryptTheInfo.py			# Encrypts the selected column
---- data_mining_methods/			# Contains the code for the various data mining methods
			+-- Apriori_timer.py		# Misnamed file Apriori association mining
			+--	Elcat.py						# Work in progress for adding the Elcat method
---- data/  			# Contains the input and output data files
------ input/			# Contains the input files
------ output/		# Contains the result files
---- anonym_methods/    					# Contains the various anonymisation methods
			+-- Anonymise_simple.py		#
			+-- Kanon_file.py					#
---- Temp/							# General purpose folder for temporary files
			+-- config.json		# The configuration file used in the actual run
```
Data mining is used to store the data mining methods, as of now it contains an
## Installing

##Other:		
For the time being the program is being moved to python 3.6
The GUI works but needs to be updated as the functionality is very basic
The defaults are level of anonymity=3, attributes we want to anonymise = 1rst 2nd and 4th (0,1,3), attributes we want to encrypt= 3rd (2)
the minimum level of supprot = 0.3 and minimum level of confidence = 0.9
These are applied to the included datafile that is census data from the census bureau database processed by the University of California Irvine.
The datafile source is the machine learning repository: https://archive.ics.uci.edu/ml/datasets/Adult

## Author

George Manakanatas

##License:

MIT License
Copyright (c) , 2015 , George Manakanatas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

- The included Apriori method was uploaded to github under the MIT License by the user asaini (abhinav saini) on the 7th of August 2013 and mildly modified.
- The logo and landing page graphics are very slightly modified versions of free vectors from [freepik](http://www.freepik.com) and [Garry Killian](https://www.freepik.com/garrykillian) on freepik respectively
