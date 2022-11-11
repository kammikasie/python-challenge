import csv #Import csv module

with open ('budget_data.csv') as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable that holds contents
    header=next(csvreader) #Read the header row first

    #Prepare variables
    months=[] #Generate list named "months" for the "Date" column
    prolosses=[] #Generate list named "prolosses" for the "Profit/Losses" column

    #Set start conditions
    total=0
    a_change=0
    m_change=0
    m_count=0
    penta1=0
    penta2=0
    penta_line1=0
    penta_line2=0
    loop1=0
    loop2=0

    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        month=row[0] #Assign column 0 as month
        proloss=row[1] #Assign column 1 as proloss
        months.append(month) #Add next line to list months
        prolosses.append(proloss) #Add next line to list prolosses
    
    m_count = len(months) #Count the total of months in the "Date" column
    #print(m_count)

    #Begin data analysis

#First loop is through list prolosses (variable loop1 as loop index counter)
for loop1 in range (m_count):
    total=total+int(prolosses[loop1]) #Calculate total amount
#print(total)

#Second loop is through list prolosses (variable loop2 as loop index counter)
for loop2 in range (m_count-1): #Restrict loop to avoid overflow (last line +1)
    a_change=a_change+(float(prolosses[loop2+1])-float(prolosses[loop2])) #Calculate sum of changes
#print(a_change/(m_count-1))
    m_change=(float(prolosses[loop2+1])-float(prolosses[loop2])) #Calculate monthly change
    if m_change>penta1: #Determine greatest increase
        penta1=m_change
        penta_line1=loop2
    else:
        penta1=penta1

#print(penta1)
#print(months[penta_line1+1])

    if m_change<penta2: #Determin greatest decrease
        penta2=m_change
        penta_line2=loop2
    else:
        penta2=penta2

#print(penta2)
#print(months[penta_line2+1])

#creating amount lines

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[penta_line1+1]} (${int(penta1)})\n\
Greatest Decrease in Profits: {months[penta_line2+1]} (${int(penta2)})\n'

print(analysis) #Results on command prompt

#Creta a text file as pybank.txt

file1=open("pybank.txt","w") #Open or if file does not exist then create file named pybank.txt
file1.writelines(analysis) #Write analysis into pybank.txt
file1.close() #Close pybank.txt write mode