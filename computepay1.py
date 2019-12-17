def computepay (h, r):
    if h > 40:
       pay = 40 * r + (h - 40) * (r * 1.5)
    else:
       pay = r * h
    p = float(pay)
    return p

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float (rate)
print (computepay (h, r))
