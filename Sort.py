#For Sorting the Student names in incresing & decreasing order of their marks 
d={'aman':39, 'ram':96, 'shyam':54, 'mohan':46, 'aaj':98}
asc=sorted(d,key=d.get)
des=sorted(d,reverse=True,key=d.get)
print(asc)
print(des)
