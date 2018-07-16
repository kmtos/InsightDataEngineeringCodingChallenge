# Table of Contents
1. [SortingData](README.md#SortingData)
2. [Input Dataset](README.md#input-dataset)
3. [Instructions](README.md#instructions)
4. [Output](README.md#output)
5. [Tips on getting an interview](README.md#tips-on-getting-an-interview)
6. [Instructions to submit your solution](README.md#instructions-to-submit-your-solution)
7. [Questions?](README.md#questions?)

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

I created a test based off of the test in "itcont.txt", with the addition of multiple entries. 
I did this to check that the sorting fully caught all defined duplicates, and that it totalled the money spent correctly.
I also wanted to test for whitespace.

