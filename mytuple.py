tp = ('AI', 'ML', 'DL', 2020)
print(tp)

a=(1,2,3,4,5,5)
print("the value repeated=", a.count(5))

print("range=", a[2:5])
a=(1,2,3,4,5)
print("no of elements=", len(a))
print("max vaue=", max(a))
print("min value=", min(a))
print("sum of all items in tuple=", sum(a))

b=(6,7,4,2,1,5,3)
print("sorted values=", sorted(b))

x=("red","green","blue") #tuple
y=list(x)                #list
y[1]="yellow"            #adding new element
x=tuple(y)               #tuple
print(x)

