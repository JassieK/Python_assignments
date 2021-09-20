s = 'jassi'
print(s.capitalize())

s = 'JASSI'
print(s.casefold())
print(s.isupper())

s = 'Jassi'
print(s.center(50))
print(s.isidentifier())
print(s.istitle())

sh = "Hello my name is Jasmit Kaur , I am pursuing my Bacherlors in technology from Techno India University"
print(sh.count("m"))
print(sh.encode())
print(sh.expandtabs(2))
print(sh.find("Kaur"))

s = " I am {age :.1f} years old "
print(s.format(age = 20.5))

si = " i have 2 guitars and 1 ukelele"
print(si.isalpha())
print(si.isalnum())
print(si.isdecimal())

n = "2341868"
print(si.isdigit())
print(si.islower())
print(n.isnumeric())
print(s.isprintable())
print(n.isspace())
print(",".join(sh,si))
print(sh.ljust(5))
print(si.lower())
print(si.lstrip(5))
print(sh.maketrans())