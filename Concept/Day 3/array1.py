import array
val=array.array("i",[1,2,3,4,5])

for i in range(0,5):
    print(val[i],end=" ")
print("\n")
for x in val:
    print(x,end=" ")    

# reverse the array
val.reverse()
print("\n reverse of array")
for x in val:
    print(x,end=" ")

# inserting an element
val.insert(2,6)
print("\n insertinon of element")
for x in val:
    print(x,end=" ") 

#copy the array 
cpyarray=array.array(val.typecode,(a for a in val))
print("\n copy of array")
for x in cpyarray:
    print(x,end=" ")

#pop the element
print("\n Pop out last element")
print("last element is:",val.pop())
for x in val:
    print(x,end=" ") 

# array slicing
print("\nsliced array",val[1:3])

# appending
val.append(6)
print("appended array")
for x in val:
    print(x,end=" ")

# finding the index of item
index=val.index(6)
print("\n the index of item is:",index)