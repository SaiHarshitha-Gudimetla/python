#adding the gst to the value
d = {'a':900, 'b': 200, 'c':1000, 'd': 1300}
gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18), d.items()))
print(gst)

#greatest numbers in the list
h = {'a':900, 'b': 200, 'c':1000, 'd': 1300}
greatest = dict(filter(lambda i: i[1]>500, h.items()))
print(greatest)

#display the booked and unbooked seats
s = {'s1': True, 's2': False, 's3': True, 's4': True, 's5': False}
booked = dict(filter(lambda i:i[1]== True, s.items()))

unbooked = dict(filter(lambda i:i[1]!= True, s.items()))
print(booked)
print(unbooked)


#sorting the dict key and values
a = {'laptop':90000, 'keyword': 2000, 'camera':100000, 'mouse': 1300}

#ascending and decending according to the keys
print(dict(sorted(a.items())))                       #ascending
print(dict(sorted(a.items(), reverse=True)))         #decending

#ascending and decending according to the values
print(dict(sorted(a.items(), key=lambda i:i[1])))                  #ascending
print(dict(sorted(a.items(), key=lambda i:i[1], reverse=True)))    #decending