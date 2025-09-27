"""A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
145 is a Strong number as 1! + 4! + 5! = 145. """


#lex_auth_01269437118923571233

def factorial(number):
    fact=1
    for i in range(1,number+1,1):
        fact*=i
    return fact


def find_strong_numbers(num_list):
    l1=[]
    strong_num=[]
    for i in num_list:
        st=str(i)
        som=0
        for j in st:
            fct=factorial(int(j))
            som+=fct
        l1.append(som)
    for i in range(len(l1)):
        
        
        if l1[i]==num_list[i]:
            strong_num.append(num_list[i])
    print(strong_num)


# num_list=[145,375,100,2,10]
num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
