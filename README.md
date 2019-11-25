<img align="right" src="./GUI/images/NEW_LAND_GRAPH1.png">
<!-- <img align="center" src="./GUI/images/PPDM_landing_large_graphic.png"> -->

# PPDM
Privacy Protecting Data Mining

##Description: 	
This is a program based on my master's thesis in the Hellenic Open University.
As it stands now it will read data from a csv file, encrypt or replace the attributes we want,
then use a simple k-anonymity method on the attributes we select
then run an Apriori algorithm on the resulting new data and return the results in a file.

##Goal:		
The goal is to provide useful for comparison of different combinations of anonymity – encryption and data mining methods. Also play around with Tkinter for the GUI

## File structure

The file structure of the project in detail.
```
.
├── anonym_methods  # anonymisation methods ( basic k-anonymity only for now)
├── config  # storing configuration files
├── data  # input and output folders
├── data_masking_methods  # encryption or replacement only for now
├── data_mining_methods  # only Apriori data mining working for now
├── functions  # various utility functions
├── GUI  # not working properly still
├── logs  # logging to file not to command line
├── temp  # temp files or intermediate steps
├── config.json  # current running ocnfiguration
├── guiTest.py  # gui start (not working)
├── main.py
└── README.md

9 directories, 4 files
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
