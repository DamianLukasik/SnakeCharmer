#-*- coding: utf8 -*-

def load_args(argumentList,args):
    import getopt
    options = []
    short_options = []
    long_options = []
    idx = 0
    for value in args:
        options.append(value[0])
        short_options.append(value[1])
        long_options.append(value[2])
        args[idx] = value[3]
        idx+=1
    try:
        arguments, values = getopt.getopt(argumentList, str(options), long_options)
        idx = 0
        for currentArgument, currentValue in arguments:
            if currentArgument in (short_options[idx], long_options[idx]):
                args[idx] = [currentValue.strip('=')]
            idx+=1
    except getopt.error as err:
        print (str(err))
    return args