s = input()
a=""
def swap_case(s):
    
    a=s.swapcase()
    return a



if len(s)<0 and len(s)>=1000:
   print("Enter valid string")
else:
   result = swap_case(s)
   print(result)

