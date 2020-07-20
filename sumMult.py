summation =0;
for i in range (1,1000):
	if (i % 5 == 0 or i %3 ==0) :
		summation = i+ summation
print "The sum is " +str(int(summation))
