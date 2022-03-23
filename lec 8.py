'''
Lecture 8
'''

#Functions reduce tedius work by doing an assigmentmultiple times

def my_funtion(a,b=0):
    print(a)
    print(b)
    
    
    result = a + b 
    
    return result
    
    
print(my_funtion(b=1, a=2))

#ex1 calculate absolute values

def cal_abs(a):
    
    if type(a) is str:
        return('wrong data type')
        
    if a >=0:
        return a
    if a < 0:
        return-a
print(cal_abs(-1))



#Ex2

def cal_s(n,m):
    
    result = 0 
    for i in range(n,m+1):
        
        result = result+i
        return(result)
        
print(cal_s(1,6))

def cal_pi(n,m):
    
    
    result = 1 
    
    for i in range(n,m+1):
        
        result = result *i
        
    return result
    
print(cal_pi(1,6))

    
#ex3

def cal_f(m):
    
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
        
print(cal_f(0))

def cal_p(n,m):
    
    return cal_f(m)/cal_f(m-n)
    
    
print(cal_p(3,5))


    