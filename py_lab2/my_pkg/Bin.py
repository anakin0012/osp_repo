import operator
def con(num):
    Bin = num
    DEC = int(Bin, 2)

    OCT = format(DEC, 'o')
    HEX = format(DEC, 'x')

    print("OCT> %s" % OCT)
    print("DEC> %d" % DEC)
    print("HEX> %s" % HEX.upper())