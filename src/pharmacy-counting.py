import csv
from prescription_drug_class_def import prescription_drug_class
from collections import defaultdict
import sys
 
INDEX_LNAME=1
INDEX_FNAME=2
INDEX_DNAME=3
INDEX_PRICE=4

full_list = []
#with open("/home/kyletos/Projects/InsightDataEngineeringCodingChallenge/insight_testsuite/tests/" + sys.argv[1] + "/input/itcont.txt") as f:
with open("input/itcont.txt") as f:
   r = csv.reader(f)
   next(r, None) #skip header
   full_list = [tuple(row) for row in r if row] #create list of tuples for each row of csv file


drug_class = prescription_drug_class(full_list, 1, 2, 3, 4)
drug_class.MergeSort(curr_list=drug_class.full_list, indecies_to_sort=[drug_class.INDEX_DNAME,drug_class.INDEX_LNAME,drug_class.INDEX_FNAME], STRorNUM="STR")
drug_class.CombineDuplicates(indecies_to_check=[drug_class.INDEX_DNAME,drug_class.INDEX_LNAME,drug_class.INDEX_FNAME])
drug_class.GetDrugPriceAndCountList()
drug_class.MergeSort(curr_list=drug_class.drug_totals_list, indecies_to_sort=[2], STRorNUM="NUM" )

drug_class.WriteSortedPersonList("output/TEST1_All_People_sorted_list.csv")
drug_class.WriteDrugCountAndTotalList("output/top_cost_drug.txt", reverse=True)

