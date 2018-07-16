# Table of Contents
1. [SortingData](README.md#SortingData)
2. [Duplicate and Whitespace Tests](README.md#input-dataset)
3. [Speed Tests](README.md#instructions)

# Sorting Data

My first step is to make a class. 
The class would contain a list that would be sorted, a dictionary of all the unique drug names, a list of all the unique drug names, and various values to be used throughout.
There are many functions in the class, including MergeSort, which sorts the list based upon any combinations of the tuple's elements in the list.
This needs to be specified in the calling of the function and the order matters.
Next there is a function that combines like elements in the sorted list. 
Along with various functions to write various outputs, there is a function that changes a list of people and their drug purchasers, and gets the unique drugs with the total money spent and the number of unique buyers. 

The sorting combines the drug name with the last name and the first name, all changed with the ".to_lower()" function, in case the data had the same names with multiple uses of capital letters within the name. 
This is done so that counting the amount of people that use the drug is simple and straightforward.
The additional alphabetizing based on the purchaser's name is used to catch any people who have bought this drug multiple times, since the output requested "the number of unique prescribers who prescribed the drug".
This also makes processing the data easy, and can be made simpler to debug.
You can write the output of this sorting is into a file by calling of the function "" in the class. This output csv file will be saved in the output directory.

# Duplicate and Whitespace Tests

I created a test, called "test_duplicates", based off of the test in "itcont.txt", with the addition of multiple entries that have random whitespace, along with entries that don't have enough elements.
I ignore all entries that don't have enough entries, or if the drug is empty, or if the last name is empty. 
I thought about cutting out data that didn't have a first name, but I figured that they could still be included in the total drug counts.
I also ignore elements that have names that are only numbers or a price that contains non-numbers, because I figured this would be improperly inputted data.
I did include drug names that included letters, because I thought that drugs being identified with a specific number seems reasonable.
I did this to check that the sorting fully caught all defined duplicates, and that it totalled the money spent correctly, with any combination of the above possible messy data entries.


# Speed Tests

I added a couple large dataset tests, called "test_large", "test_larger", "test_largest", to see how long it takes.
I don't have the memory on my computer to use the entire dataset on my computer, so I made incrementally bigger ones.
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


