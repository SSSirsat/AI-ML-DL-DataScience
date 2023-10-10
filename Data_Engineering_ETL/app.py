import os
import glob
# print(os.listdir())
# print(os.listdir('data/retail_db/'))
# # print(files = [f for f in os.listdir('data/retail_db/') if os.path.isdir(f)])

# files = os.listdir('data/retail_db/')
# for f in files:
#     if f.endswith('.json'):

#         print(f"json file is present name is {f} size is {f.__sizeof__()}")
# path = 'data/retail_db/'

# for i in glob.glob(f'{path}/*'):
#     if os.path.isdir(i):
#         print(i)

line = 'shubham suryakant sirsat is 3 the most importanat 1 person in the world'

words = line.split(' ') 
s = line.strip("3")
print(s)
print(words)
8766627894
print(', '.join(['ss','sd','df']))

# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

number= 8
for i in range(number):
    for j in range(number-i-1):
        print(" ", end="")
    for j in range(2*i-1):
        print("*",end="")
    print()