def sum(n):
	sum=0
	while n>0:
		r=n%10
		sum+=r
		n//=10
	return sum
n=int(input())
print(sum(n))
