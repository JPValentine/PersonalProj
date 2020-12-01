from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {})#string of HTML code

def isBinary(x):
    b = {'0','1'}
    t = set(x)
    if b==t or t=={'0'} or t=={'1'}:
        return True
    else:
        return False

def bin_to_hex(request):
    try:
        if request.POST['in']:
            myStr=(request.POST['in'])
            myStr2=myStr
            if isBinary(myStr)==False:
                myStr="Bad Input!"
                return render(request,"bin_to_hex.html",{'result': myStr})
            myStr=int(myStr,2)
            myStr=hex(myStr)
            res= myStr2+" = "+myStr
            return render(request,"bin_to_hex.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"bin_to_hex.html",{'result': res})
    return render(request, "bin_to_hex.html", {})

def bin_to_oct(request):
    try:
        if request.POST['in']:
            myStr=(request.POST['in'])
            if isBinary(myStr)==False:
                myStr="Bad Input!"
                return render(request,"bin_to_oct.html",{'result': myStr})
            fin=int(myStr,2)###converting the bin to dec
            i=0
            li=[0]*20
            while(fin !=0):###then converting the dec to octal
                li[i] = fin %8
                fin = int(fin/8)
                i+=1
            li.reverse()
            del li[0:(len(li)-i)]
            res=myStr +" = "+(''.join(map(str,li)))
            return render(request,"bin_to_oct.html",{'result': res})


    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"bin_to_oct.html",{'result': res})
    return render(request,"bin_to_oct.html",{})

def bin_to_dec(request):
    try:
        if request.POST['in']:
            myStr=(request.POST['in'])
            myStr2=myStr
            if isBinary(myStr)==False:
                myStr="Bad Input!"
                return render(request,"bin_to_dec.html",{'result': myStr})
            res=myStr2+" = "+str(int(myStr,2)-0)
            return render(request,"bin_to_dec.html",{'result': res})
    except Exception as e:
        res=""
        return render(request,"bin_to_dec.html",{'result': res})
    return render(request,"bin_to_dec.html",{})

def hex_to_bin(request):
    try:
        if request.POST['in']:
            hex=(request.POST['in'])
            try:
                dec=int(hex,16)
                b=bin(dec).replace("0b","")
                res=hex+" = "+b
                return render(request,"hex_to_bin.html",{'result': res})
            except ValueError as e:
                res="Bad Input!"
                return render(request,"hex_to_bin.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"hex_to_bin.html",{'result': res})
    return render(request,"hex_to_bin.html",{})

def hex_to_oct(request):
    try:
        if request.POST['in']:
            hex=(request.POST['in'])
            try:
                fin=int(hex,16)
                i=0
                li=[0]*20
                while(fin !=0):###then converting the dec to octal
                    li[i] = fin %8
                    fin = int(fin/8)
                    i+=1
                li.reverse()
                del li[0:(len(li)-i)]
                res=hex+" = "+(''.join(map(str,li)))
                return render(request,"hex_to_oct.html",{'result': res})
            except ValueError as e:
                res="Bad Input!"
                return render(request,"hex_to_oct.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"hex_to_oct.html",{'result': res})
    return render(request,"hex_to_oct.html",{})

def hex_to_dec(request):
    try:
        if request.POST['in']:
            hex=(request.POST['in'])
            try:
                dec=int(hex,16)
                res=hex+" = "+str(dec)
                return render(request,"hex_to_dec.html",{'result': res})
            except ValueError as e:
                res="Bad Input!"
                return render(request,"hex_to_dec.html",{'result': res})
    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"hex_to_dec.html",{'result': res})
    return render(request,"hex_to_dec.html",{})

def oct_to_hex(request):
    try:
        if request.POST['in']:
            if request.POST['in']:
                octal=int(request.POST['in'])
                octList=[int(x) for x in str(octal)]
                flag=True
                for i in range(len(octList)):
                    if int(octList[i])>7 or int(octList[i])<0:
                        flag=False
                if flag==False:
                    res="Bad Input!"
                    return render(request,"oct_to_hex.html",{'result': res})
                else:
                    dec=0
                    octList.reverse()
                    for i in range(len(octList)):###convert to dec
                        octList[i]=int(octList[i])###changing index to an int
                        dec=dec+(octList[i]*(8**i))
                    dec=hex(dec)
                    res=str(octal)+" = "+str(dec)
                    return render(request,"oct_to_hex.html",{'result': res})
    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"oct_to_hex.html",{'result': res})
    return render(request,"oct_to_hex.html",{})

def oct_to_bin(request):
    try:
        if request.POST['in']:
            if request.POST['in']:
                octal=int(request.POST['in'])
                octList=[int(x) for x in str(octal)]
                flag=True
                for i in range(len(octList)):
                    if int(octList[i])>7 or int(octList[i])<0:
                        flag=False
                if flag==False:
                    res="Bad Input!"
                    return render(request,"oct_to_bin.html",{'result': res})
                else:
                    dec=0
                    octList.reverse()
                    for i in range(len(octList)):###convert to dec
                        octList[i]=int(octList[i])###changing index to an int
                        dec=dec+(octList[i]*(8**i))
                    dec = bin(dec).replace("0b","")
                    res=str(octal)+" = "+str(dec)
                    return render(request,"oct_to_bin.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"oct_to_bin.html",{'result': res})
    return render(request,"oct_to_bin.html",{})

def oct_to_dec(request):
    try:
        if request.POST['in']:
            octal=int(request.POST['in'])
            octList=[int(x) for x in str(octal)]
            flag=True
            for i in range(len(octList)):
                if int(octList[i])>7 or int(octList[i])<0:
                    flag=False
            if flag==False:
                res="Bad Input!"
                return render(request,"oct_to_dec.html",{'result': res})
            else:
                dec=0
                octList.reverse()
                for i in range(len(octList)):###convert to dec
                    octList[i]=int(octList[i])###changing index to an int
                    dec=dec+(octList[i]*(8**i))
                    res=str(octal)+" = "+str(dec)
                return render(request,"oct_to_dec.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"oct_to_dec.html",{'result': res})
    return render(request,"oct_to_dec.html",{})

def dec_to_hex(request):
    try:
        if request.POST['in']:
            dec=int(request.POST['in'])
            h=hex(dec)
            res=str(dec)+ " = "+str(h)
            return render(request,"dec_to_hex.html",{'result': res})
    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"dec_to_hex.html",{'result': res})
    return render(request,"dec_to_hex.html",{})

def dec_to_oct(request):
    try:
        if request.POST['in']:
            fin=int(request.POST['in'])
            x=fin
            i=0
            li=[0]*20
            while(fin !=0):###then converting the dec to octal
                li[i] = fin %8
                fin = int(fin/8)
                i+=1
            li.reverse()
            del li[0:(len(li)-i)]
            res=str(x) +" = "+(''.join(map(str,li)))
            return render(request,"dec_to_oct.html",{'result': res})
    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"dec_to_oct.html",{'result': res})
    return render(request,"dec_to_oct.html",{})

def dec_to_bin(request):
    try:
        if request.POST['in']:
            dec=int(request.POST['in'])
            b=bin(dec).replace("0b","")
            res=str(dec)+" = "+str(b)
            return render(request,"dec_to_bin.html",{'result': res})
    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"dec_to_bin.html",{'result': res})
    return render(request,"dec_to_bin.html",{})

def hex_calc(request):
    return render(request,"hex_calc.html",{})

def bin_calc(request):
    return render(request,"bin_calc.html",{})

def oct_calc(request):###this one is a mess =/
    try:
        if request.POST['o1'] and request.POST['o2'] and request.POST['op']:
            oct1=int(request.POST['o1'])
            oct2=int(request.POST['o2'])
            operation=str(request.POST['op'])
            oct1split=[int(x) for x in str(oct1)]###turning input into str lists
            oct2split=[int(x) for x in str(oct2)]
            flag=True
            loopLength=0
            for i in range(len(oct1split)):
                if int(oct1split[i])>7 or int(oct1split[i])<0:
                    flag=False
            for i in range(len(oct2split)):
                if int(oct2split[i])>7 or int(oct2split[i])<0:
                    flag=False
            if flag==True and (len(oct2split)!=len(oct1split)):###making the list the smae length
                if(len(oct2split)>len(oct1split)):
                    for i in range(len(oct2split)-len(oct1split)):
                        oct1split.insert(0,"0")
                else:
                    for i in range(len(oct1split)-len(oct2split)):
                        oct2split.insert(0,"0")

            if(flag==False):
                res="Bad Input!"
                return render(request,"oct_calc.html",{'result': res})
            else:
                oct1split.reverse()
                oct2split.reverse()
                for i in range(len(oct1split)):###convert all strings back into int in lists
                    oct1split[i]=int(oct1split[i])
                    oct2split[i]=int(oct2split[i])

                endlist = []

                for i in range(len(oct1split)+1):###filling endlist with placeholder 0's
                    endlist.insert(0,0)

                if operation=="+":
                    for i in range(len(oct1split)):
                        if (oct1split[i]+oct2split[i])>=8:
                            endlist[i]=endlist[i]+(oct1split[i]+oct2split[i])-8
                            endlist[i+1]=1
                        else:
                            endlist[i]=endlist[i]+oct1split[i]+oct2split[i]

                    for i in range(len(endlist)):
                        if endlist[i]==8:
                            endlist[i]=0
                            endlist[i+1]=endlist[i+1]+1
                elif operation=="-":
                    if oct1<oct2:###wont work if oct1 is smaller than oct2
                        res="First Octal Number must be bigger than Second Octal"
                        return render(request,"oct_calc.html",{'result': res})
                    elif oct1==oct2:
                        res="0"
                        return render(request,"oct_calc.html",{'result': res})
                    else:
                        oct1=0
                        oct2=0
                        for i in range(len(oct1split)):###convert to dec
                            oct1=oct1+(oct1split[i]*(8**i))
                            oct2=oct2+(oct2split[i]*(8**i))

                        fin=oct1-oct2###subtracting newly formed decimals
                        i=0
                        while(fin !=0):
                            endlist[i] = fin %8
                            fin = int(fin/8)
                            i+=1

                endlist.reverse()

                if endlist[0]==0:
                    endlist.pop(0)

                res=''.join(map(str, endlist))
                return render(request,"oct_calc.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res="error"
        return render(request,"oct_calc.html",{'result': res})
    return render(request,"oct_calc.html",{})

def ieee_754_calc(request):
    return render(request,"ieee_754.html",{})

def ones_compliment(request):
    try:
        if request.POST['in']:
            myStr=(request.POST['in'])
            if isBinary(myStr)==False:
                myStr="Bad Input!"
                return render(request,"ones_compliment.html",{'result': myStr})
            li=list(myStr)
            hold=""
            for i in range(len(li)):
                if li[i]=="1":
                    hold+="0"
                else:
                    hold+="1"
            res=myStr+" = "+hold
            return render(request,"ones_compliment.html",{'result': res})
    except Exception as e:
        res=""
        return render(request,"ones_compliment.html",{'result': res})
    return render(request,"ones_compliment.html",{})


def ip_class(request):
    try:
        if request.POST['ip1'] and request.POST['ip2'] and request.POST['ip3'] and request.POST['ip4']:
            v1 = int(request.POST['ip1'])
            v2 = int(request.POST['ip2'])
            v3 = int(request.POST['ip3'])
            v4 = int(request.POST['ip4'])
            if (v1<=126):
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Class A!"
            elif v1>=128 and v1<=191 and v2>=1 and v4>=1 and v4<=255:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Class B!"
            elif v1>=192 and v1<=223 and v3>=1 and v3<=254 and v4<=255:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Class C!"
            elif v1>=224 and v1<=239:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Class D!"
            elif v1>=240 and v1<=255 and v3<=255:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Class E!"
            elif v1==127:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Loopback Address!"
            elif v1==255 and v4==255:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = Broadcast Address!"
            else:
                res=str(v1)+"."+str(v2)+"."+str(v3)+"."+str(v4)+" = not working"
            return render(request,"ip_class.html",{'result': res})

    except Exception as e:
        print("ERROR",e)
        res=""
        return render(request,"ip_class.html",{'result': res})
    return render(request,"ip_class.html",{})
