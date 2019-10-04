


# prediction algorithm
def predict(f1, f2):
    for i in f1:
        for j in f2:
            if f1[i] == f2[j]:
                print('pattern matched')
            else:
                print('not match')



# print the List
def printList(logList):
    for i in range(len(logList)):
        print(logList[i])




# read from file
def readFile(f1):
    logList = []    
    with open('Log.txt') as f1:
        logList = f1.readlines()
    logList.append([x.strip() for x in logList])

    printList(logList)
    
    # predict the nxt 
    predict(f1, f2) 

def readFile(f2):
    iplog = []
    with open('iplog.txt') as f2:
        iplog = f2.readlines()
    iplog = [x.strip() for x in iplog]

    printList(iplog)

# main module 
if __name__ == '__main__':

# FileHandling
    # create a file & append
    f1 = open('Log.txt', 'a+')
    f2 = open('iplog.txt', 'a+')

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
    # print(medicineList)
    # medicine = int(input())
    
    # appeding in the list 
    lst.append(symtoms)
    lst.append(environment)
    # lst.append(medicine)


    # print
    print(lst)
    print(symtomsList[symtoms-1], environmentList[environment-1])


    # data insert into the file
    f1.write(str(lst))
    f1.write('\n')


    # read the file
    readFile(f1)
    readFile(f2)

    # file close
    f1.close()
    f2.close()

    

