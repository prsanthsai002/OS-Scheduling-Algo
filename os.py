c=[]
a=[]
b=[]
p=int(input("How many processess:"))
for i in range(p):
    c.append("p%d" %i)
for i in range(p):
    a.append(int(input("Arrival time of the process %d is:" %i)))
print("Arrival times are :",a)
for i in range(p):
    b.append(int(input("Burst time of the process %d is:" %i)))
print("Arrival times are :",a)
print("Processess are:",c)
for i in range(3):
    for j in range(len(b)):
        if(i==0):
            b[j]=b[j]-6
            if(b[j]==0):
                print("Process %d terminated",)
        if(i==1):
            b[j]=b[j]-10
        if(i==2):
            b[j]=b[j]-b[j]
print(b)