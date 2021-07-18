# Membership
set1 = {1,2,3,4,'hello'}
print(6 in set1)
print(4 in set1)

# Add
set1.add(6)
print(set1)

# Remove
set1.remove(4)
print(set1)

# Union
set2 = {1,'apple'}
print(set1|set2)

# Clear
set1.clear()
print(set1)

# Intersection
A = {1,2,3,4}
B = {1,5,7,3}
print(A & B)

# Difference
print(A - B)
print(B - A)

# Sym.Difference
print(A^B)

# Size
print(len(A))

# Copy
C = A.copy()
print(C)