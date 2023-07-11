l=[]
salary = 0
for i in range(7):
    input_hours= int(input())
    l.append(input_hours)
for j in l:
    salary= salary+(j*100)
    if j >8:
        diff = j-8
        salary = salary+(diff*15)
if sum(l)>40:
    total_diff = sum(l)-40
    salary = salary +(total_diff*25)
if l[0]>0:
    total_money= l[0]*100
    salary+= total_money/2
if l[6]>0:
    total_mon= l[6]*100
    div = total_mon/2
    salary+= div/2
print(int(salary))
        
             
