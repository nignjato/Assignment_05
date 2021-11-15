#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Nik Ignjatovic, 2021-11-14, Updated File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
strtxt = '' # User data
dicRow = {} # Declare dictionary
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Load existing data
        objFile = open(strFileName,'r')
        print('File Data:')
        for row in objFile:
            lstRow = row.strip()
            print(lstRow)
        objFile.close()
        selection = input('Replace existing data with loaded file? (y/n): ')
        if selection == 'y':
            lstTbl.clear()
            objFile = open(strFileName,'r')
            for row in objFile:
                lstRow = row.strip()
                lstTbl.append(lstRow)
            print('File data loaded.\n')
            objFile.close()
        elif selection == 'n':
            print('Ok. Data not replaced with file.\n')
        else:
            print('Error.\n')
        objFile.close()
        pass
    elif strChoice == 'a':
        # Add data to the table (2d-list) each time the user wants to add data
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID': intID,'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print(lstTbl)
        for row in lstTbl:
            print(row)
        pass
    elif strChoice == 'd':
        # Delete a record if the user chooses to 
        print('')
        deletekey = int(input('Enter the ID of the record you wish to delete: '))
        for index in range(len(lstTbl)):
           if lstTbl[index]['ID'] == deletekey:
              del lstTbl[index]
              break
        pass
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        for row in lstTbl: 
            strtxt += str(row) + '\n'
        strtxt = strtxt[:-1]
        objFile = open(strFileName,'a')
        objFile.write(strtxt)
        objFile.close()
        print('\nData Saved.') 
    else:
        print('Please choose either l, a, i, d, s or x!')

