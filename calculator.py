#!/usr/bin/env python3

import sys

print('Your income is:',sys.argv[1])

try:
    income =int(sys.argv[1])
    if income < 0:
        raise ParameterError
       
except:
    print("Parameter Error")
   
s_insur = 0
thred = 3500
payg = income - s_insur - thred
i_tax = [0.03,0.1,0.2,0.25,0.3,0.35,0.45]
ss_del = [0,105,555,1005,2755,5505,13505]

if payg < 1500:
    case = 0
elif payg < 4500:
    case = 1
elif payg < 9000:
    case = 2
elif payg < 35000:
    case = 3
elif payg < 55000:
    case = 4
elif payg < 80000:
    case = 5
else:
    case = 6

tax = payg * i_tax[case] - ss_del[case]
print('Totally ',format(tax, ".2f"),'  should be paid!')

