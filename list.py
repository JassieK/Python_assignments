my = ['Guitar','processors','amps','mics']
ess =['colours','books','pens']
my.append("chords")
print(my)
list = my.copy()
print(list)
print(my.count("Guitar"))
my.extend(ess)
print(my)
print(my.index("books"))
my.insert(2,"interface")
print(my)
my.pop(3)
print(my)
my.remove("Guitar")
print(my)
my.reverse()
print(my)
n = [4,3,2,1]
n.sort()
print(n)

my.clear()