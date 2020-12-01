print("yut")
"""
This is me messing around with bitwise operators and checking different uses
for each sign

Python 3.8
JP Valentine
9/13/2020
"""

a=255 #1111 1111
b=0   #0000 0000
c=170 #1010 1010
d=85  #0101 0101
e=15  #0000 1111
f=240 #1111 0000

def setBlank():
    """
    resets each variable to their original values
    """
    a=255 #1111 1111
    b=0   #0000 0000
    c=170 #1010 1010
    d=85  #0101 0101
    e=15  #0000 1111
    f=240 #1111 0000

def bitVal(n):
    """
    prints int no bigger than 255 and displays the bit value of
    the int
    :param n:takes an int to be printed
    :return: returns a string with the bit value
    """
    x=128
    n=abs(n)
    new=""#new value to be printed
    for i in range(8):
        if n>=x:
            n=n-x
            new=new+"1"
        else:
            new=new+"0"
        x=x/2
    return new

def parity(n):
    """
    parity checking function that can do 64 bit numbers prints out 1 or zero at
    the end
    "param n" number to be checked
    """
    n ^= n>>32
    n ^= n>>16
    n ^= n>>8
    n ^= n>>4
    n ^= n>>2
    n ^= n>>1
    print(n&1)

def bitSwap(n,i,j):
    """
    swaping bits on a number
    :param n: number to have bits swapped
    :param i: first position in which the bit should be swapped
    :param j: second position in whick the bit should be swapped
    """
    if (n>>i)&1 != (n>>j)&1:#shift right on n until i and j postions then check if that bit is the same
        bitMask = (1<<i) | (1<<j)
        n ^=bitMask
    return n


#write code here
setBlank()
print("Before ones compliment: ",c," ",bitVal(c))
b=~c
print("After ones compliment: " ,b," ",bitVal(b))
setBlank()
print("Before ones compliment: ",d," ",bitVal(d))
b=~d
print("After ones compliment: " ,b," ",bitVal(b))
setBlank()
b=a>>3
print(b)
print(bitVal(b))
b=0
if (a>>8)==b:
    print("Worked!")
q=0
print(bitVal(~q))
print("-------------")
parity(254)
bitSwap(255,8,1)
