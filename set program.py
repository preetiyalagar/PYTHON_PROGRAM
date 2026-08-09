#using set - python collection
mset={"Java", "Python", "CPP"}
print(mset)
print("length:", len(mset))

for x in mset:
    print(x)
mset.add("PHP")
print(mset)

mset.discard("CPP")
print(mset)

myset={1,2,3}
myset.clear()
print(myset)

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A.union(B))