a = int(input("INPUT A NUMBER :"))
if a<=0 or a>10:
    print("PLEASE ENTER NUMBER BETWEEN 1 AND 10")
else:
    for i in range(10):
        print('{} * {} = {}'.format(a,i+1,a*(i+1)))