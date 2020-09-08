print("This program shows the least amount of coins required to have the sum of your money value!")
zenny=0.0
zenny= input('Enter your money value: ')

print "Your money value is: " , zenny
zenny=zenny+0.001
quarters=0
dimes=0
nickels=0
pennies=0
flag=True

while flag:
    if zenny >= 0.25:
        quarters+=1
        zenny=zenny-0.25
    else:
        flag=False

flag=True
while flag:
    if zenny>=0.10:
        dimes+=1
        zenny=zenny-0.10
    else:
        flag=False

flag=True
while flag:
    if zenny>=0.05:
        nickels+=1
        zenny=zenny-0.05
    else:
        flag=False

flag=True
while flag:
    if zenny>=0.01:
        pennies+=1
        print "zenny before: ",zenny
        zenny=zenny-0.01
        print "zenny after: ",zenny
        print "counted!!"
    else:
        flag=False


print "Number of quarters: ", quarters
print "Number of dimes: ", dimes
print "Number of nickels: ", nickels
print "Number of pennies: ", pennies
