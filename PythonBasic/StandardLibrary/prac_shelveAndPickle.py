import shelve

d = shelve.open("shelvetest1")
d["3"] = 4
d["5"] = "6"
list(d.items())
d.close()

d2 = shelve.open("shelvetest1")
print(list(d2.items()))
d2.close()