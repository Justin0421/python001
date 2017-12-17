#!/usr/bin/env python3

import sys

#constants
i_tax = (0.03,0.1,0.2,0.25,0.3,0.35,0.45)
ss_del = (0,105,555,1005,2755,5505,13505)
s_insur = 0.08 + 0.02 + 0.005 + 0 + 0 +0.06 
thred = 3500
#get parameters
w_nb = []
w_income = []
for arg in sys.argv[1:]:
    w = arg.split(':')
    #convert to int and test error
    try:
        int_wnb = int(w[0])
        int_wincome = int(w[1])
        if int_wnb <= 0 or int_wincome <= 0:
            raise ParameterError
    except:
        print('ParameterError')
    #get parameter lists
    w_nb.append(w[0])
    w_income.append(w[1])

#function check income class and return
def check_case(payg):
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
    return case

#calculate PAYG 
def cal_payg(income):
    payg = int(income)*(1 - s_insur) - thred
    return payg

#calculate tax
def cal_tax(payg,cs):
    tax = float(payg) * i_tax[cs] - ss_del[cs]
    return tax

if __name__ == '__main__':
    payg = []
    tax = []
    i = 0
    for income in w_income:
        p = cal_payg(income)
        if int(p) < 0:
            t = 0
        else:
            payg.append(p)
            cs = check_case(p)
            t = cal_tax(p,cs)
        tax.append(t)
        #output result
        final_income = int(income)*(1-s_insur) - t
        print(w_nb[i],' : ', format(final_income, ".2f"))
        i = i + 1
