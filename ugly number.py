def getNthUgly(n):
	ugly = [0]*n
	ugly[0]= 1
	i2=i3=i5=0
	m2 = 2
	m3 = 3
	m5 = 5
	
	for i in range(1,n):
		ugly[i]= min(m2,m3,m5)
		if ugly[i] == m2:
			i2+=1
			m2 = ugly[i2]*2
		if ugly[i] == m3:
			i3+=1
			m3 = ugly[i3]*3
		if ugly[i] == m5:
			i5+=1
			m5 = ugly[i5]*5
	return ugly[-1]
print(getNthUgly(5))
	