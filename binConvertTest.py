#!/usr/bin/python
import random
from bitstring import BitArray
import time

def twosComplement(bitTest):
    neg=bitTest[0]

    if (neg=='0'):
        bitTest=bitTest[1:]
        return strToUint(bitTest)
    else:
        bitTest=list(bitTest)
        reverse=False
        for i in range(len(bitTest)):
            x=len(bitTest)-1-i
            if (reverse==False and bitTest[x]=='1'):
               reverse=True
            elif reverse:
               if (bitTest[x]=='1'):
                   bitTest[x]='0'
               else:
                   bitTest[x]='1'
        return -strToUint(bitTest)


def strToUint(bitTest):
        uint = 0
        exp=1
        for i in range(-(len(bitTest)-1),1):
            if (bitTest[-i]==str(1)):
                uint+=exp
            exp*=2
        return uint

def randBin(size):
       bitTest=""
       for i in range(0,size):
           bitTest+=str(random.randint(0,1))
       return bitTest

def check(converted,uint):
        if (converted==uint):
            print "Good!"
            return True
        else:
            print "Wrong! The answer was "+uint+ " not "+converted
            return False

def add_dur(durs,dur):
       durs.append(dur)
       print "That took you "+str(dur)

def print_avg_time(durs):
    total=0
    for d in durs:
       total+=d
    print "average time for responses to "+str(len(durs))+" was "+str(total/len(durs))

def printHex(bitTest):
    str=""
    for i in range(0,len(bitTest),4):
        str+=bitTest[i:i+4]+" "
    return str

def do_bit_test(size):
    durs=[]
    for i in range(1,10):
        bitTest=randBin(size)
        t=  int(time.time())
        converted= raw_input("Convert "+printHex(bitTest)+" unsigned:")

        uint  = strToUint(bitTest)
        dur = ( int(time.time())-t)
        if (not(check(converted,str(uint)))):
            exp=1
            for i in range(-(size-1),1):
                if (bitTest[-i]==str(1)):
                    print exp
                exp*=2
            break
        add_dur(durs,dur)
    print_avg_time(durs)

def do_convert_to_hex():
    durs=[]
    for i in range(1,10):
       bitTest=randBin(16)
       print bitTest
       t=  int(time.time())
       converted = raw_input("Convert "+printHex(bitTest)+" to hex :")
       dur = ( int(time.time())-t)
       uint  = strToUint(bitTest)
       print uint
       ans='{0:x}'.format(int(uint))
       if(not(check(converted.rstrip(),ans))):
           break
       add_dur(durs,dur)
    print_avg_time(durs)

def do_convert_to_twos_complement():
    durs=[]
    for i in range(1,10):
       bitTest=randBin(4)
       print bitTest
       t=  int(time.time())
       converted = raw_input("Convert "+printHex(bitTest)+" to twos complement:")
       dur = ( int(time.time())-t)
       uint = twosComplement(bitTest)
       print uint
       if(not(check(converted.rstrip(),str(uint)))):
           break
       add_dur(durs,dur)
    print_avg_time(durs)

def do_bin_add():
    durs=[]
    for i in range(1,10):
        bitTest=randBin(8)
        bitTest1=randBin(8)
        print bitTest
        t=  int(time.time())
        converted = raw_input("Add "+printHex(bitTest)+" and "+printHex(bitTest1)+":")
        dur = ( int(time.time())-t)
        uint = twosComplement(bitTest)
        uint2 = twosComplement(bitTest1)
        print uint+uint2
        if(not(check(converted.rstrip(),str(uint+uint2)))):
           break
        add_dur(durs,dur)
    print_avg_time(durs)

def do_hex_add():
    pass

random.seed()
print "Binary Tester\n"
input=""
while (input==""):
    input = raw_input("1. 16 bit binary conversion test\n2. Convert to hex\n3. Twos Complement\n4. Do Bin Add\n5. Do Hex add\n6. 8 bit binary conversion test\n7. exit\n? ")
    if (input=="1"):
        do_bit_test(16)
    elif (input=="2"):
        do_convert_to_hex()
    elif (input=="3"):
        do_convert_to_twos_complement()
    elif (input=="4"):
        do_bin_add()
    elif (input=="5"):
        do_hex_add()
    elif (input=="6"):
        do_bit_test(8)
    elif (input=="7"):
        break
    else:
        print "Unknown Option:"+input
        input=""
