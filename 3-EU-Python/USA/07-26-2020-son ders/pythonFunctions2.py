# square = lambda x:x**2  
# print(square(3))

# def square_2(x):
#     print(x**2)

# square_2(3)
# takeAverage = lambda x,y:(x+y)/2
# print(takeAverage(3,5))

# def test(x):
#     if x % 2 != 0:
#         return 'odd'
#     else:
#         return 'even'

# output = test(5)
# print(output)

# reverser = lambda x : x[::-1]
# print(reverser('clarusway'))

# print(list('clarusway'))

# iterable = 'clarusway'

# reverser = (lambda x:x[::-1])(iterable)
# print(reverser)

# lst = [0,1,2,3,4,5,6]
# for i in filter(lambda x:x%2==0,lst):
#     print(i,i+2,end=" ")

# import string
# print(string.punctuation)

# from random import choice

# print(choice(string.punctuation))

# def functioner(emoji=""):
#     return lambda message: print(message,emoji)

# myPrint_smile = functioner()
# myPrint_smile('hello')

# Since lambda function printing message emoji, don't print out anything. It will print

# status = [1,2,3]
# if status:
#     print("''Hello World!")
# else:
#     print("'Hello worlds'??")
# try:
#     a = int(input('Could you please give me a number? : '))
# except ValueError as e:
#     print('Something wrong happened... {}'.format(e))
# else:
#     b = 100
#     print(a+b)
# finally:
#     print('hey you learned this')

# for i in range('x'):
#     print(i)
# import os
# os.system('clear')
# while True:    
#     try:
#         a = int(input('Hey user, give me the first number : '))
#         b = int(input('Hey user, give me the second number : '))
#         division = a/b
#     except ValueError:
#         print('something went wrong...valueerror')
#     except ZeroDivisionError:
#         print('something went wrong...this is most probably zeroDivision')
#     except:
#         print("Don't forget to close the parantheses")
#     else:
#         print(division)
#         break
#     finally:
#         print('Everything went well. Great job.')

# with open('fileRead/names.csv') as f:
#     for line in f:
#         print(line.strip().split(','))

lst= [1,3,3,5,7,3,4,5,6,7]

def repeatsOrNot(a):
    dct={}
    for i in lst:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    for i in dct:
        if dct[i]>1:
            print('repeating elements')
            return
    print('no repeats')

repeatsOrNot(lst)

