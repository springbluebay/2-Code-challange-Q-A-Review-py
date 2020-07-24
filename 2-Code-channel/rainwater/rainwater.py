# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. (edited)

ls=[0,1,0,2,1,0,1,3,2,1,2,1] 

def rainwater(ls):
    a=ls[0]
    biriken=0
    count=0
    for i in ls:
        if a > i:
            if isbigger(ls[count+1:], a):
                biriken += (a-i)
            else:
                a = max(ls[count:])
                biriken += (a-i)
        else:
            a=i
        count +=1
    return biriken

def isbigger(ls2, a):
    for j in ls2:
        if j >=a:
            return True
            
print(rainwater(ls))