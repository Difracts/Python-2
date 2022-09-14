a = int(input("insert size of  R (n>=5) : "))
n,count = [],2
for i in range(a//2+1):
    row = ""
    if i == 0 or i == a//2:
        for j in range(a//2+1):
            row+="*"
    else:
        row+="*"
        for j in range(a//2):
            row+=" "
        row+="*"
    n.append(row)

for i in range(a//2):
    row = "*"
    for j in range(count):
        row+=" "
    row+="*"
    n.append(row)
    count+=1
for i in n:
    print(i)