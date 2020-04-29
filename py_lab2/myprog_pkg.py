from my_pkg.Bin import *
from my_pkg.UI import *

while(True) :
    num = int(input("Select menu: 1)conversion 2)union/intersection 3)exit ?"))
    if num == 1:
        Bin = input("input binary number : ")
        con(Bin)
    elif num == 2:
        list1 = list(input("1st list: "))
        list2 = list(input("2nd list: "))
        UandI(list1, list2)
    elif num == 3:
        exit(0)