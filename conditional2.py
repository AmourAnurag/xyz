# problem - 1
# a=int(input("enter the first angel :"))
# b=int(input("enter the second angel :"))
# c=int(input("enter the third angel :"))
# s=a+b+c
# if (s!=180):
#     print("invalid triangle")
# else:
#     print("valid triangle")


# problem -2 
# n= float(input("enter a number :"))
# x=abs(n)
# print("absolute value is :",x)

#problem-3 
# l=int(input("enter length of triangle"))
# b=int(input("enter breath of triangle"))
# area=l*b
# per=2*(l+b)
# if area==per:
#     print("both are same")
# else:
#     print("both are not same")

#problem-4 
x1=int(input("input x1 :"))
x2=int(input("input x2 :"))
x3=int(input("input x3 :"))
y1=int(input("input y1 :"))
y2=int(input("input y2 :"))
y3=int(input("input y3 :"))

a=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)

if(a==0):
    print("collinear")
else:
    print("not collinear")