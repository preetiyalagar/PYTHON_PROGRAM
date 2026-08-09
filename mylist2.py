m=['Apple','Orange','Cherry']
m.reverse()
print("Reverse List:",m)
m.append('Banana')
print("Appending list:",m)
n=m.copy()
print("Copying list from one to another:",n)
m.insert(1, 'Kiwi')
print("Adding new value:",m)
m.pop(1)
print("Removing:",m)
m.sort()
print("sorting",m)
print(m[1:4])
for x in m:
    print(x)
if 'Apple' in m:
    print("Yes! Apple is there")
else:
    print("Sorry! Apple is not in list")
item=['PC', 'Laptop', 'LED', 'LCD']
print(item)
print("Total no of items in list:",len(item))

print("odd list")
mylist=[1,2,3,4,5,6]
for x in mylist:
    if(x%2!=0):
        print(x)

print("even list")
mylist=[1,2,3,4,5,6]
for x in mylist:
    if(x%2==0):
        print(x)