def computepay(h,r):
    if h > 40:
        extra = h - 40
        gross_pay = ((h-extra) * rate) + (extra*(rate*1.5))
    else:
        gross_pay = h * rate

    return gross_pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))
p = computepay(hrs,rate)
print("Pay",p)
