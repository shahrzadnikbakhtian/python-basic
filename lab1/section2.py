name =input("what is your name?")
cookies = input("how many cookies would you like to have?")
print("hi " + name)

my_var_more="cookies " * 50
my_var_low= "cookies " * 10
my_var=""
num_cookies= int(cookies)
for i in range(num_cookies):
    my_var += "cookies "
if 0<num_cookies<10:
    print("Are you sure it's enough? here are your cookies: " + my_var)

elif 10<num_cookies<20:
    print("I agree cookies are delicious! here are your cookies: " + my_var)

elif 20<=num_cookies<=50:
    print("Be careful, it's getting too much here are your cookies: " + my_var)

elif num_cookies>50:
    print("No way, it’s getting too much’ here are your cookies: " + my_var_more)

else:
    print("Something must be wrong, I give you 10 cookies: " + my_var_low)


