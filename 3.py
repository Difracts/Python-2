a = int(input("Input a dog's age in human years: "))
count = 0
for i in range(1, a + 1):
    if i <= 2 :
        count+=10.5
    else:
        count+=4
print("The dog's age in dog's years is " + str(int(count)))