
#* Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#* Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#* Change Items
# Once a set is created, you cannot change its items, but you can add new items.

#* Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#* Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#* Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #pop() in sets not remove last item
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#set cannot delete
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#* Join Two Sets
#union is same update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#* The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#* Set Methods
# add()	                            Adds an element to the set
# clear()	                        Removes all the elements from the set
# copy()	                        Returns a copy of the set
# difference()	                    Returns a set containing the difference between two or more sets
# difference_update()	            Removes the items in this set that are also included in another, specified set
# discard()	                        Remove the specified item
# intersection()	                Returns a set, that is the intersection of two other sets
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                    Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                    Returns whether this set contains another set or not
# pop()	                            Removes an element from the set
# remove()	                        Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                        Update the set with the union of this set and others