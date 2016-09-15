a=input("enter a string: ")
check=set()
result=[]
for i in a:
	if i not in check:
		check.add(i)
		result.append(i)
print(", ".join(result))
