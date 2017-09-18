# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:54:07 2017

@author: ARSHABH SEMWAL
"""
import random

password_type=input('password type: simple | complex ')

char_set = {'nums': '0123456789',
            'small': 'abcdefghijklmnopqrstuvwxyz',
            'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }
                        
# get the length of password for above input
if password_type == 'simple' :
    min_len= input('min length of password')
    max_len= input('max length of password')
   
    min_lwr=input('min no of lower case character')
    max_lwr=input('max no of lower case character')

    min_upr=input('min no of UPPER CASE character')
    max_upr=input('max no of UPPER CASE character')
    while True :
        lwr = random.randrange(int(min_lwr) , int(max_lwr))
        upr = random.randrange(int(min_upr) , int(max_upr))
        ttl = lwr + upr
        if ttl >= int(min_len) and ttl <= int(max_len):
            break    
    pswd = [0]*ttl
    for i in range(lwr):
        pswd[i] = char_set['small'][random.randrange(0,26)]
    for i in range(lwr,upr+lwr):
        pswd[i] = char_set['big'][random.randrange(0,26)]
    random.shuffle(pswd)
    pswd = ''.join(pswd)
    print(pswd)

    

else: 

    min_len= input('min length of password')
    max_len= input('max length of password')
    
    min_no_int= input('min no of numerics')
    max_no_int= input('max no of numerics')
    
    min_lwr=input('min no of lower case character')
    max_lwr=input('max no of lower case character')
    
    min_upr=input('min no of UPPER CASE character')
    max_upr=input('max no of UPPER CASE character')
    
    min_spl=input('min no of special character')
    max_spl=input('max no of special character')

    while True :
        no = random.randrange(int(min_no_int) , int(max_no_int))
        lwr = random.randrange(int(min_lwr) , int(max_lwr))
        upr = random.randrange(int(min_upr) , int(max_upr))
        spl= random.randrange(int(min_spl) , int(max_spl))
        total = [no , lwr , upr ,spl]
        len_p = sum(total)
        if len_p >= int(min_len) and len_p <= int(max_len):
            break
    pswd = [0]*len_p
    for i in range(no):
        pswd[i] = char_set['nums'][random.randrange(0,10)]
    for i in range(no, lwr+no):
        pswd[i] = char_set['small'][random.randrange(0,26)]
    for i in range(no+lwr,upr+no+lwr):
        pswd[i] = char_set['big'][random.randrange(0,26)]
    for i in range(upr+no+lwr,len_p):
        pswd[i] = char_set['special'][random.randrange(0,29)]
    random.shuffle(pswd)
    pswd = ''.join(pswd)
    print(pswd)

   
            
