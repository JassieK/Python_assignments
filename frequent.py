import operator
s = input("Please Enter a string ")

def most_frequent(str):
    d = dict()
    for key in str:
        if key not in d:
            d [key] = 1
        else:
            d[key] += 1
    return d
new = most_frequent(s)
sort = dict( sorted(new.items(), key=operator.itemgetter(1),reverse=True))

print(sort)
