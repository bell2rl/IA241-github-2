'''
Lab 3
list and set
'''

str_list = ['a', 'd', 'e', 'b', 'c']
str_list.sort()

print(str_list)

#3.2

str_list.append('f')
print(str_list)

#3.3

str_list.remove('d')
print(str_list)

#3.4

print(str_list[2])

#3.5

my_list = ['a','123',123, 'b','8', 'False', False, 123, None, 'None']

print(len(set(my_list)))

#3.6

print(len("This is my third python lab".split()))

#3.7

num_list = [12,32,43,35]
print(num_list [2])
print(num_list[0])

#or you could do it this way

num_list_dos = [12,32,43,35]
num_list_dos.sort()
print(num_list_dos[0])
print(num_list_dos[-1])

#3.8

gameboard_list = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
print(gameboard_list[1])
gameboard_list[1] = [0, 1, 0]
print(gameboard_list)

# or you could also do this

gameboard_list = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
print(gameboard_list[1][1])
gameboard_list[1][1] = 1
print(gameboard_list)
