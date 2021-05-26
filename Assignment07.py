# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and erorr handling
# Github Link: https://github.com/Tekpro007/IntroToProg-Python-Mod07
# ChangeLog (Who,When,What):
# Kyle Gilpin, 5.24.2021, Created script with header information and outline of script
# Kyle Gilpin, 5.25.2021, Created functions
#Kyle Gilpin, 5.25.2021, Created presenation portion of script

#------------------------------#
import pickle

#Data-----------------------#
strFileName = 'ShoppingList.dat'
lstCustomer = []
strItem = ''
strCost = ''

#Processor
def save_data_to_file(file_name, list_of_data):
    """ Saves data to a file

       :param file_name: (string) with name of file:
       :param list_of_data: (list) you want filled with file data:
   """
    file = open(file_name, 'ab')
    pickle.dump(list_of_data, file)
    file.close()

def read_data_from_file(file_name):
    """ read data to a file

       :param file_name: (string) with name of file:
   """
    try:
        file=open(file_name, 'rb')
        lstCustomer= pickle.load(file)
        file.close()
        return lstCustomer
    except FileNotFoundError as e:
        return 'File not found'

#Presenation------------#
print('Please input data into shopping list')
strItem = str(input("Enter Shopping list item: "))
strCost = str(input("Enter cost: "))
lstCustomer = [strItem, strCost]

save_data_to_file(strFileName, lstCustomer)

print(read_data_from_file(strFileName))
