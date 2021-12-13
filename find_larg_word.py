txt="hello olrd miiiiiiohan xzy aaaaaaaa s"

lis=txt.split(' ')
print(lis)

def find_larg(lis,n):
	max=len(lis[0])
	for i in range(1,n):
		if len(lis[i])>max:
			max=len(lis[i])
		
	return max
			
n=len(lis)
ans=find_larg(lis,n)
#print(ans)

for i in lis:
	if ans==len(i):
		print(i)
	