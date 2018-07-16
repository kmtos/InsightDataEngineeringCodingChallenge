import csv
from prescription_drug_class_def import prescription_drug_class
from collections import defaultdict
import sys
import time

start = time.time()
 
INDEX_LNAME=1
INDEX_FNAME=2
INDEX_DNAME=3
INDEX_PRICE=4

##########################################
# Reading in the data as a list of tuples
##########################################
full_list = []
with open("input/itcont.txt") as f:
   for row in csv.reader(f):
      if len(row) != 5: 
         continue
      if len("".join(row[INDEX_DNAME].split())) == 0 or len("".join(row[INDEX_LNAME].split())) == 0: 
         continue
      if "".join(row[INDEX_LNAME].split()).isdigit() or "".join(row[INDEX_FNAME].split()).isdigit():
         continue
      if not row[INDEX_PRICE].strip().replace(".", "", 1).isdigit():
         continue
      full_list.append( (row[0],row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip()) )


###############################################
# Executing the functions to get the tuple:
# (drug, num unique persons, total purchases)
##############################################
drug_class = prescription_drug_class(full_list, 1, 2, 3, 4)
drug_class.MergeSort(curr_list=drug_class.full_list, indecies_to_sort=[drug_class.INDEX_DNAME,drug_class.INDEX_LNAME,drug_class.INDEX_FNAME], STRorNUM="STR")
drug_class.CombineDuplicates(indecies_to_check=[drug_class.INDEX_DNAME,drug_class.INDEX_LNAME,drug_class.INDEX_FNAME])
drug_class.GetDrugPriceAndCountList()
drug_class.MergeSort(curr_list=drug_class.drug_totals_list, indecies_to_sort=[2], STRorNUM="NUM" )


#################
# Output writing
#################
drug_class.WriteSortedPersonList("output/TEST1_All_People_sorted_list.csv")
drug_class.WriteDrugCountAndTotalList("output/top_cost_drug.txt", reverse=True)

end = time.time()
print ("TIME:", end - start )
