s="john marta james Morgan Adam Maria huang"
s1=[word[0].upper() + word[1:] for word in s.split()]
Var=" ".join(s1)
print(s1)
s2="Names"
for line in [s2]:
    print("{:+^90}".format(s2))
for line in [s1]:
    print("{:>90} \n {:>90} \n {:>90} \n {:>90} \n {:>90} \n {:>90} \n {:>90}" .format(*line))

St = "name=Amanda=sssss&age=32&&salary=1500&currency=quro"
St_my="name&Amanda=sssss"
St_1=St.split("&")
St1=St_1.split("&")
St2=St1[0]
St3=St1[1]
St4=St2.split("&")
St5=St3.split("&")
St6=St4[1]
St6=St6.split("=")
St8=St5[1]
St8=St8.split("=")
St9=St5[1]
St9=St9.split("=")
V2=St1+St6+St8+St9
keys=[]
values=[]
for i, j in enumerate(V2):
    if i% 2==0:
        keys.append(j)
    else:
        values.append(j)
print(dict(zip(keys, values)))

