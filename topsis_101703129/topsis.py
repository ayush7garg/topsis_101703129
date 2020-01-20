import numpy as np
import csv
from io import StringIO

def topsis(data,weights,impacts):
    number_of_weights = len(weights)
    for i in range(number_of_weights):
        weights[i] = float(weights[i])
    rows=[]
    x2=[]
    row_num=0
    
    buffer = StringIO()
    data.to_csv(buffer)
    buffer.seek(0) 
    
    data = csv.reader(buffer)
    fields = next(data)
    for row in data:
        rows.append(row[2:])
        row_num = row_num+1
    col_num = len(rows[0])
    for i in range(0,row_num):
        for j in range(0,col_num):
            rows[i][j] = float(rows[i][j])
    
    for i in range(0,col_num):
        sum1=0
        for j in range(0,row_num):
            sum1 = sum1 + rows[j][i]*rows[j][i]
        sum1 = sum1**0.5
        x2.append(sum1)
    
    for i in range(0,col_num):
        for j in range(0,row_num):
            rows[j][i] = rows[j][i]/x2[i]
    
    for i in range(0,col_num):
        for j in range(0,row_num):
            rows[j][i] = rows[j][i]*weights[i]
    
    v1=[]
    v2=[]
    
    arr = np.array(rows)
    
    for i in range(0,col_num):
        if impacts[i]=='+':
            v1.append(max(arr[:,i]))
            v2.append(min(arr[:,i]))
        elif impacts[i]=='-':
            v1.append(min(arr[:,i]))
            v2.append(max(arr[:,i]))
    
    
    s1=[]
    s2=[]
    
    for j in range(row_num):
        sum1 = 0
        sum2 = 0
        for i in range(col_num):
            sum1 = sum1 + (arr[j][i]-v1[i])*(arr[j][i]-v1[i])
            sum2 = sum2 + (arr[j][i]-v2[i])*(arr[j][i]-v2[i])
        sum1 = sum1**0.5
        sum2 = sum2**0.5
        s1.append(sum1)
        s2.append(sum2)
    
    s = []
    for i in range(len(s1)):
        s.append(s1[i]+s2[i])
    
    p=[]
    for i in range(len(s1)):
        p.append(s2[i]/s[i])
    
    
    m = p.index(max(p))
    print("Object",m+1,"is the best.")
