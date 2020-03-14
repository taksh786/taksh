def updat(a,*ar):
    new=dict()
    new.update(a)
    for i in ar:
        new.update(i)
    return new
a={'1':2,'2':3,'4':4,'5':5}
b={'6':7,'8':8,'0':5}
c=updat(a,b)
print(c)
for i,j in c.items():
    print(i," ",j)
