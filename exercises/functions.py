# Write your solution for 1.4 here!

def is_prime(x):
	i=0
	a=0
	while i<x:
		i=i+1
		if x%i==0:
			print("can be divided by"+str(i))
			a=a+1
		else:
			print("can not be divided by"+str(i))
	if a==2:
		print("it's a prime!!")
	else:
		print("not a prime!!")	
     
is_prime(7)	     
