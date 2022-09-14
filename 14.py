sum , count = 0 , 0
n = int(input())
while n!=0:
    sum+=n
    count+=1
    n = int(input())
if count==0:
    print("ENTER AT LEAST ONE NUMBER")
else:
    print('sum is : {} , and average is : {} . '.format(sum,sum/count))