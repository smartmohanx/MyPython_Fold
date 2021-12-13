
#Final largest number!

#your code goes here

lis=[2,55,88,6,99,34,1]


def find_larg(lis,n):
	max=lis[0]
	for i in range(1,n):
		if lis[i]>max:
			max=lis[i]
	return max
	
n=len(lis)
ans=find_larg(lis,n)
print(lis)
print("The largest:",ans)

lis.remove(ans)

n=len(lis)
s_l=find_larg(lis,n)
print("2nd largest:",s_l)


lis.remove(s_l)

n=len(lis)
t_l=find_larg(lis,n)
print("3rd largest:",t_l)