user_number=input("how many numbers do you have?")
quantity= int(user_number)
sum= 0
for i in range(quantity):
    num= input("what is the " + str(i+1) + ". number?")
    sum= sum + int(num)

avg=sum/quantity
avg_float= format(avg , ".2f")
print(f"this is the average: {avg_float}")


    