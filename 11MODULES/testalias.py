import mathmod as mm

print (mm.y)
print (mm.mul(10,20))
print (mm.add(10,20))

# This will throw the error as already the alias being created.
# we cannot original name since alias being generated.
# if accessing then it generates the name error
print(mathmod.x)