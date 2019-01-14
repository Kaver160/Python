def neifunc(*args):
    if args==0:
        return('argument ne ykazan')
    if args==1:
        return(args)
    if args>1:
        slovar = {}
        for arg in args:
            if type(arg) not in slovar.keys():
                slovar[type(arg)] = 1
            else:
                slovar[type(arg)] += 1
        return(slovar)
test=neifunc(1)
print(test)
