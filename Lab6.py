'''
Lab 6 
'''

#3.1


for i in range(6):
    
    
    if i !=3:
        
        print(i)
        
#3.2

result = 1

for i in range(1,6):
    
    result = result * i
    
    print(result)
    
#3.3

answer = 0 

for i in range (1,6):
    answer = answer + i
    
    print(answer)
    
#3.4 

answer = 1

for i in range (3,9):
    answer = answer * i
    
    print(answer)
    
#3.5

answer = 1

for i in range (4,9):
    answer = answer * i
    
    print(answer)

#3.6


result = 0 
for word in 'this is my 6th string'.split():
    print(word)
    result = result + 1 
    
print(result)
        
