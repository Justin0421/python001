#!/usr/bin/env python3

import sys

class Config(object):
    def __init__(self, configfile):
        with open(configfile) as file:
            count = 0
            self._config = {}
            for line in file:
                count += 1
                L =  line.replace(" ","").split('=')
                #print(line)
                self._config[L[0]] = L[1]
        #for k,v in self._config.items():
            #print(k,v)
    def get_config(self, value):
        #for k,v in self._config.items():
            #print(k, v)
        #print(type(value))
        #print(value)   
        return self._config.get(value,'not exist key')
    
class UserData(object):
    def __init__(self, userdatafile):
        with open(userdatafile) as file:
            count = 0
            self._userdata = {}
            for line in file:
                count += 1
                L =  line.replace(" ","").split(',')
                self._userdata[L[0]] = L[1]

    def get_userdata(self, value):
        return self._userdata.get(value,'not exist key')
    def calculator(self)
        pass
    def dumptofile(self,outputfile)
        pass
#get all parameters
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]

#try class
config = Config(configfile)
print(config.get_config('JiShuH'))
userdata = UserData(userdatafile)
print(userdata.get_userdata('101'))
