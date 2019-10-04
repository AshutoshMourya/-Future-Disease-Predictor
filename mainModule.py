

# read from file
def readFile():
    f = open('Log.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    # algo here

# main module 
if __name__ == '__main__':

# FileHandling
    # create a file & append
    f = open('Log.txt', 'a+')
   

 # list for dataset
    lst = []
    symtomsList = ['Body-Pain', 'Cough & Cold', 'Fever', 'Headache', 'Inflamation', 'dizzing']
    environmentList = ['Hot',  'Cold',  'Humitnity',  'Rainy',  'Snoozy']
    medicineList = ['Paracetamol',  'Nemoslide',  'Dichlomo',  'Phenil']

# dataset from user 
    # for the symtoms
    print(symtomsList)
    symtoms = int(input())

    # climate or whether
    print(environmentList)
    environment = int(input())

    # medicine 
    print(medicineList)
    medicine = int(input())
    
    # appeding in the list 
    lst.append(symtoms)
    lst.append(environment)
    lst.append(medicine)


    # print
    print(lst)
    print(symtomsList[symtoms-1], environmentList[environment-1], medicineList[medicine-1])

    # data insert into the file
    f.write(str(lst))
    f.write('\n')

    # file close
    f.close()

    # read the file
    readFile()


