a = int(input("insert size of O (n>=5) : "))
n = [[""] for i in range(a)]
for i in range(a):
    if i==0 or i==a-1:
        n[i]+=" "
        for j in range(a-2):
            n[i]+="*"
        n[i]+=" "
    else:
        n[i]+="*"
        for j in range(a-2):
            n[i]+=" "
        n[i]+="*"
for i in n:
    for j in i:
        print(j,end = "")
    print()