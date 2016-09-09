import json
from datetime import datetime
with open('salary.json') as data_file1:    
    data1 = json.load(data_file1)
with open('height.json') as data_file2:    
    data2 = json.load(data_file2)
b=[]
flist=[]
n=len(data1)
m=len(data2)
for i in range(0,n):
			a=[]
			a.append(data1[i]['First_name'])
			a.append(data1[i]['Last_name'])
			a.append(data1[i]['Date_of_birth'])
			a.append(data1[i]['Salary'])
			a.append(data2[i]['Height'])
			b.append(a)
p=len(b)
b.sort(key=lambda sl: (datetime.strptime(sl[2],"%Y-%m-%d"),sl[3],sl[4]))
#print(b)
for i in range (0,len(data1)):
	string="First Name: "+str(b[i][0])+ ",Last Name: "+str(b[i][1])+",DOB: " +str(b[i][2])+",Salary: " + str(b[i][3])+",Height: " + str(b[i][4]) + '\n'
	flist.append(string)
fstring="".join(flist)
#print(flist)
print(fstring)

	
