def computepay(h,r):
    if h>40:
        reg=40*r
        extra=(h-40)*1.5*r
        pay=reg+extra
    else:
        pay=h*r
    return pay


hrs = input("Enter Hours:")
h=float(hrs)
rate=input("Enter Rate:")
r=float(rate)
p = computepay(h,r)
print(p)
