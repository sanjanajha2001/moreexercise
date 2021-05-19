def is_harshad_number(a):
    n=a
    c=n
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    if(c%sum==0):
        print("is harshad number")
    else:
        print("it is not a harshad number")
is_harshad_number(17)