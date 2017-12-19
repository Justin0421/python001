#!/usr/bin/env python3

import sys
import os

#get input parameters
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
index = args.index('-o')
outputfile = args[index+1]

#test files' existence
if os.path.exists(configfile) == False:
    raise 'File not exist'
if os.path.exists(userdatafile) == False:
    raise 'File not exist'

#get other unchange-parameters for calculation
tax_rate = (0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45)
kouchu = (0, 105, 555, 1005, 2755, 5505, 13505)

class Config(object):
    def __init__(self, configfile):
        with open(configfile) as file:
            count = 0
            self._config = {}
            # test file format and parameter, then convert to dict  
            try:
                for line in file:
                    count += 1
                    L = []
                    L =  line.replace(" ","").split('=')
                    if len(L) != 2:
                        raise 'File format error'
                    print(type(L[1]))
                    self._config[L[0]] = float(L[1])
            except:
                print('ParameterError', 'in', line)
                exit()
    #visit dict value       
    def get_config(self, value):   
        return self._config.get(value,'not exist key')
    
class UserData(object):
    def __init__(self, userdatafile):
        with open(userdatafile) as file:
            count = 0
            self._userdata = {}
            # test file format and parameter, then convert to dict 
            try:
                for line in file:
                    count += 1
                    L = []
                    L =  line.replace(" ","").split(',')
                    if len(L) != 2:
                        raise 'File format error'
                    self._userdata[L[0]] = int(L[1])
            except:
                print('ParameterError', 'in', line)
                exit()            
    #visit dict value
    def get_userdata(self, value):
        return self._userdata.get(value,'not exist key')
    #calculate and yield?
    def calculator(self):
        pass
    #calculate case, input payg(float)
    def cal_case(self,value):
        if value < 1500:
            case = 0
        elif value < 4500:
            case = 1
        elif value < 9000:
            case = 2
        elif value < 35000:
            case = 3
        elif value < 55000:
            case = 4
        elif value < 80000:
            case = 5
        else:
            case = 6
        return case
    
    #calculate jifei, input income(int)
    def cal_jifei(self,value)
        jifei_rate = 
        JL = self.get_config('JiShuL')
        print(type(JL))
        if income < self.get_config('JiShuL')  
            jifei = JL * 
    def dumptofile(self,outputfile):
        pass


#try class
config = Config(configfile)
print(config.get_config('JiShuH'))
userdata = UserData(userdatafile)
print(userdata.get_userdata('101'))
