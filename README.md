# Table of Contents
1. [SortingData](README.md#SortingData)
2. [Duplicate and Whitespace Tests](README.md#input-dataset)
3. [Speed Tests](README.md#instructions)
4. [Implementation](README.md#implementation)
# Sorting Data

My first step is to make a class. 
The class attributes would include a list that would be sorted, a dictionary and/or a list of all the unique drug names with the prescriber counts and dollars spent, and various values to be used throughout.
There are multiple functions in the class, including MergeSort, which sorts the list based upon any combinations of the tuple's elements in the list.
The list of indecies needs to be specified, and in order, in the calling of the function.
Next there is a function that combines like elements in the sorted list. 
Along with various functions to write various outputs, there is a function that changes a list of people and their drug purchasers, and gets the unique drugs with the total money spent and the number of unique buyers. 

The sorting combines the drug name with the last name and the first name, all changed with the ".to_lower()" function, in case the data had the same names with multiple uses of capital letters within the name. 
This is done so that counting the amount of people that use the drug is simpler and amore straightforward.
The additional alphabetizing based on the purchaser's name is used to catch any people who have bought this drug multiple times, since the output requested "the number of unique prescribers who prescribed the drug".
The list alphabetized, one can processing the data more easily, and can be made simpler to debug.
Additionally, the lists can be saved, so that if the dataset is large, one can only sort the list to then later recall and use.
This stepwise implementation makes the process quicker for processing large datasets
You can write the output of this sorting is into a file by calling of the function "WriteSortedPersonList" in the class and providing the location plus name of the file along.

# Duplicate and Whitespace Tests

I created a test, called "test_duplicates" that was based off of the test in "itcont.txt", but with the addition of entries that have random whitespace, along with entries that don't have enough elements or incorrect values for certain fields.
I ignore all entries that don't have enough entries, or if the drug is empty, or if the last name is empty. 
I thought about cutting out data that didn't have a first name, but I figured that they could still be included in the total drug counts.
I also ignore elements that have names that are only numbers or a price that contains non-numbers, because I figured this would indicate improperly inputted data.
I did include drug names that contained letters, because I thought that drugs being identified with a specific number seems reasonable.
I did this to check that the sorting fully caught all defined duplicates, and that it totalled the money spent correctly, with any combination of the above possible messy data entries.


# Speed Tests

I added a couple larger dataset tests, called "test_large", "test_larger", "test_largest", to see how long the program takes to execute.
I don't have enough memory on my computer to process the entire dataset, so I made incrementally bigger ones.
Below are my tests:

TIME: 0.0003688335418701172
[PASS]: test_1 top_cost_drug.txt

TIME: 0.0004494190216064453
[PASS]: test_duplicates top_cost_drug.txt

TIME: 0.4426097869873047
[PASS]: test_large top_cost_drug.txt

TIME: 5.097609043121338
[PASS]: test_larger top_cost_drug.txt

TIME: 367.963036775589
[PASS]: test_largest top_cost_drug.txt
[Mon Jul 16 14:04:46 PDT 2018] 5 of 5 tests passed


# Implementation

To execute this scrip, just run the "./run_tests.sh" command in the "insight_testsuite/" directory. 
I was uncertain on where to point the input and output file locations to, but when investigating the above testing script, I noticed where it looked and pointed my scripts to read and write to "insight_testsuite/input/" and "insight_testsuite/output/", respectively.
This enabled the test to run correctly. 
I have written 3 files that are relevant to this problem:

1) run.sh  -  This simply runs the following python script.

2) pharmacy-counting.py - This reads in the csv file and creates and instance of the class. Afterwards, it calls the relevant functions.

3) prescription_drug_class_def.py - This contains the definition of the class called in the above python script. There are more functions than are used, due to having changed my methods several times.

Thank you for reading, and I hope everything works.

Kyle Tos
