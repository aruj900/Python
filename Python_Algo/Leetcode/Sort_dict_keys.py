dict = {"Aruj": 20,"Rahul":56,"fom":12}
age = list(dict.keys())
age.sort(key= lambda i: (dict[i],i))

print(age)