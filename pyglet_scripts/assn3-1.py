hrs = raw_input("Enter Hours:\n")
h = float(hrs)

rate = raw_input("Enter Pay Rate:\n")
r = float(rate)

if h <= 40 :
  pay = r * h 
elif h > 40 :
  pay = (r * 40) + ((1.5 * r) * (h - 40))
else :
  print "try again" 


print pay
