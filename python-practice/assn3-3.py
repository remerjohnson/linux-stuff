score = raw_input("Enter Score:\n")
s = float(score)

if s < 0 :
  print "Score out of range"
elif s > 1 :
  print "Score out of range"
elif s < .6 :
  print "F"
elif s >= 0.9 :
  print "A"
elif s >= 0.8 :
  print "B"
elif s >= 0.7 :
  print "C"
elif s >= 0.6 :
  print "D"
