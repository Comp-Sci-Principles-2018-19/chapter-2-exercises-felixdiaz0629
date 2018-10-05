P=10000
n=12
r=.08
t=input ("Number of years: ")
t=int(t)
A = P * ( 1 + r/n )** (n * t)
print(A)