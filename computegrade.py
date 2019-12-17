def computegrade(score):
  try:
    score = float(input("Enter Score Grade:"))
    if score >= 1.0:
      grade = ('Bad Score')
    elif score >= 0.9:
      grade = ('A')
    elif score >= 0.8:
      grade = ('B')
    elif score >= 0.7:
      grade = ('C')
    elif score >= 0.6:
      grade = ('D')
    else:
      grade = ('F')
  except:
    grade = ('Bad Score')
  return grade

a = computegrade(0.95)
print(a)

b = computegrade('perfect')
print(b)

c = computegrade(10.0)
print(c)

d = computegrade(0.75)
print(d)

e = computegrade(0.5)
print(e)
