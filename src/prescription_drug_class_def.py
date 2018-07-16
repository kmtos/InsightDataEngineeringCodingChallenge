import csv
import string


class prescription_drug_class(object):

   def __init__(self, drug_list, index_last_name, index_first_name, index_drug_name, index_drug_price):
      self.full_list = drug_list
      self.INDEX_LNAME = index_last_name
      self.INDEX_FNAME = index_first_name
      self.INDEX_DNAME = index_drug_name
      self.INDEX_PRICE = index_drug_price

   def MergeSort(self, curr_list, indecies_to_sort, STRorNUM="STR"):
      """
      This function follows the basic merge sort technique. It sorts based upon the ordering of the 
      elements specified in "indecies_to_sort", which are elements in the tuples contained in the list.
      It does NOT combine terms if the compared elements are equal, but it is generalized to work with 
      numbers of strings, as specified in "STRorNUM".
      """
      if len(curr_list) > 1:
         mid = len(curr_list)//2
         left_list  = curr_list[:mid]
         right_list = curr_list[mid:]
      
         self.MergeSort(left_list,  indecies_to_sort, STRorNUM=STRorNUM)
         self.MergeSort(right_list, indecies_to_sort, STRorNUM=STRorNUM)
      
         index_l  = 0
         index_r  = 0
         index_a  = 0
         length_l = len(left_list )
         length_r = len(right_list)

         while index_l < length_l and index_r < length_r:
            if STRorNUM == "STR": 
               name_l = ''
               name_r = ''       
               for i in indecies_to_sort:
                  name_l += str(left_list[ index_l][i])
                  name_r += str(right_list[index_r][i])
               name_l = "".join(name_l.split())
               name_r = "".join(name_r.split())
               name_l = name_l.lower()
               name_r = name_r.lower()
            elif STRorNUM == "NUM": 
               name_l = 0
               name_r = 0       
               for i in indecies_to_sort:
                  name_l += float(left_list[ index_l][i])
                  name_r += float(right_list[index_r][i])
            if name_l > name_r:
               curr_list[index_a] = right_list[index_r]
               index_r += 1
            else:
               curr_list[index_a] = left_list[index_l]
               index_l += 1
            index_a += 1

 
         while index_l < length_l:
            curr_list[index_a] = left_list[index_l]
            index_a += 1
            index_l += 1
           
         while index_r < length_r:
            curr_list[index_a] = right_list[index_r]
            index_a += 1
            index_r += 1
         

   def CombineDuplicates(self, indecies_to_check):
      """
      This combines prices of like terms based upon the element indecies stated in "indecies_to_check".
      """
      list_to_delete = []
      for i in range(len(self.full_list)-1):
         if i in list_to_delete: continue
         j = i + 1
         checkIfDiff = False
         for ind in indecies_to_check:
            if self.full_list[i][ind] != self.full_list[j][ind]: 
               checkIfDiff = True
         while not checkIfDiff:
            self.full_list[i] = (self.full_list[i][:self.INDEX_PRICE] +
                                (float(self.full_list[i][self.INDEX_PRICE]) + float(self.full_list[j][self.INDEX_PRICE]),) +
                                self.full_list[i][self.INDEX_PRICE+1:])
            list_to_delete.append(j)
            j +=  1
            for ind in indecies_to_check:
               if self.full_list[i][ind] != self.full_list[j][ind]: 
                  checkIfDiff = True
            
      for i in reversed(list_to_delete):
         del self.full_list[i]

   def GetDrugPriceAndCountDict(self):
      """
      This gets the drug purchase and count itotals in the form of a dict.
      """
      curr_dname = self.full_list[0][self.INDEX_DNAME]
      curr_dname = curr_dname.replace(" ", "__")
      self.drug_totals_dict = {}      
      self.drug_totals_dict[curr_dname] = [0,0]
      for row in self.full_list:
         if row[self.INDEX_DNAME] == curr_dname:
            self.drug_totals_dict[curr_dname][0] += 1
            self.drug_totals_dict[curr_dname][1] += float(row[self.INDEX_PRICE] )
         else:
            curr_dname = row[self.INDEX_DNAME] 
            curr_dname = curr_dname.replace(" ", "__")
            self.drug_totals_dict[curr_dname] = [1,float(row[self.INDEX_PRICE])]

   def GetDrugPriceAndCountList(self):
      """
      This gets the drug purchase and count totals in the form of a list.
      """
      curr_dname = self.full_list[0][self.INDEX_DNAME]
      self.drug_totals_list = []
      totalPurchases = 0
      countUnique = 0
      for row in self.full_list:
         if row[self.INDEX_DNAME] == curr_dname:
            totalPurchases += float(row[self.INDEX_PRICE] )
            countUnique    += 1
         else:
            self.drug_totals_list.append( (curr_dname, countUnique, totalPurchases) )
            curr_dname     = row[self.INDEX_DNAME] 
            totalPurchases = float(row[self.INDEX_PRICE])
            countUnique    = 1
      self.drug_totals_list.append( (curr_dname, countUnique, totalPurchases) )


   def WriteSortedPersonList(self, outFileName, reverse=False):
      """
      Writes out the sorted list of the data provided to a file.
      """
      with open(outFileName, 'w') as sortedFile:
         wr = csv.writer(sortedFile)
         wr.writerow(["id","prescriber_last_name","prescriber_first_name","drug_name","drug_cost"])
         if not reverse:
            for row in self.full_list:  wr.writerow(row)
         else:
            for row in reversed(self.full_list):  wr.writerow(row)


   def WriteDrugCountAndTotalDict(self, outFileName, reverse=False, decimals=False):
      """
      Writes out the drug_totals_dict to a file specified. To loop
      backwards, then enable the boolean option.
      """
      with open(outFileName, 'w') as sortedFile:
         wr = csv.writer(sortedFile)
         wr.writerow(["drug_name","num_prescriber","total_cost"])
         if not reverse:
            for k,v in self.drug_totals_dict.items():          
               if decimals: wr.writerow( (str(k.replace("__"," ")), v[0], "{0:.2f}".format(v[1])) )
               else:        wr.writerow( (str(k.replace("__"," ")), v[0], "{0:.0f}".format(v[1])) )
         else:
            for k,v in reverse(self.drug_totals_dict.items()): 
               if decimals: wr.writerow( (str(k.replace("__"," ")), v[0], "{0:.2f}".format(v[1])) )
               else:        wr.writerow( (str(k.replace("__"," ")), v[0], "{0:.0f}".format(v[1])))
  

   def WriteDrugCountAndTotalList(self, outFileName, reverse=False, decimals=False):
      """
      Writes out the drug_totals_list to a file specified. To loop
      backwards, then enable the boolean option.
      """
      with open(outFileName, 'w') as sortedFile:
         wr = csv.writer(sortedFile)
         wr.writerow(["drug_name","num_prescriber","total_cost"])
         if not reverse:
            for row in self.drug_totals_list:
               if decimals: wr.writerow( (row[0], row[1], "{0:.2f}".format(row[2])) )
               else:        wr.writerow( (row[0], row[1], "{0:.0f}".format(row[2])))
         else:
            for row in reversed(self.drug_totals_list):  
               if decimals: wr.writerow( (row[0], row[1], "{0:.2f}".format(row[2])) )
               else:        wr.writerow( (row[0], row[1], "{0:.0f}".format(row[2])) )

   def ConvertDrugTotalDictToList(self):
      """
      If the drug totals are already in dict form, this function 
      converts it to a list.
      """
      self.drug_totals_list = []
      for k,v in self.drug_totals_dict.items():
         self.drug_totals_list.append( (k.replace("__"," "), v[0], v[1]) )


